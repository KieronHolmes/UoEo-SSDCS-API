"""
Provides access to the Microservice functionality of the system.
"""
from json.decoder import JSONDecodeError

import requests
from drf_spectacular.utils import extend_schema
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ResultSerializer


class MicroserviceSearchView(APIView):
    """
    get:
        Fetches information from the remote CERN Document Server based on the user query.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ResultSerializer

    @extend_schema(
        summary="Queries CERN Document Server",
        description="Searches the CERN Document Server for documents matching the given query.",
        tags=["Microservice"],
    )
    def get(self, request, *args, **kwargs):
        """
        Handles the processing and formatting of data between the client and the remote CERN API.
        """
        status_response = status.HTTP_200_OK
        try:
            req = requests.get(
                f"https://cds.cern.ch/search?p={kwargs['query']}&of=recjson&ot=title,authors,creation_date"
            )
            try:
                json_formatted = {
                    "query": kwargs["query"],
                    "results": [
                        {
                            "title": item["title"]["title"],
                            "created_at": item["creation_date"],
                            "authors": [
                                {"name": author["full_name"]}
                                for author in item["authors"]
                                if author["full_name"] is not None
                            ],
                        }
                        for item in req.json()
                        if item["title"] is not None
                    ],
                }
                result = ResultSerializer(json_formatted, many=False).data
            except JSONDecodeError:
                result = {"error": "Your query resulted in 0 search results."}
                status_response = status.HTTP_404_NOT_FOUND
        except (HTTPError, ConnectionError, Timeout, RequestException):
            result = {
                "error": "Unfortunately an error occurred when attempting to connect to the upstream host."
            }
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(result, status=status_response)
