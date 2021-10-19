from rest_framework.views import APIView
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from json.decoder import JSONDecodeError
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from rest_framework import status


class MicroserviceSearchView(APIView):
    """
    get:
        x
    """
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        summary="Queries CERN Document Server",
        description="Searches the CERN Document Server for documents matching the given query.",
        tags=["Microservice"]
    )
    def get(self, request, *args, **kwargs):
        dict_response = {"query": kwargs['query']}
        status_response = status.HTTP_200_OK
        try:
            req = requests.get(f"https://cds.cern.ch/search?p={kwargs['query']}&of=recjson&ot=title,authors,creation_date")
            try:
                json_formatted = [{"title": item['title']['title'], "created_at": item['creation_date'], "authors": [author['full_name'] for author in item['authors']]} for item in req.json() if item['title'] is not None]
                dict_response['count'] = len(json_formatted)
                dict_response['results'] = json_formatted
            except JSONDecodeError:
                dict_response['error'] = "Your query resulted in 0 search results."
                status_response = status.HTTP_404_NOT_FOUND
        except HTTPError:
            dict_response['error'] = "Upstream API returned a HTTP error."
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        except ConnectionError:
            dict_response['error'] = "Connection error."
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        except Timeout:
            dict_response['error'] = "Connection to upstream host timed out."
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        except RequestException:
            dict_response['error'] = "A Request Exception was raised."
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(dict_response, status=status_response)
