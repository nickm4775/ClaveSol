from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_size = 10


class MediumSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 15
    page_size = 15


class LargeSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 20
    page_size = 20
