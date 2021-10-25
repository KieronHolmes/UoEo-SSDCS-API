"""
Provides customised pagination parameters for the Documents item.
"""
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    Sets the custom parameter name to be used for the returned page size, as well as the defaults to be used if the page_size parameter is not supplied.
    """

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 25
