from rest_framework.pagination import PageNumberPagination


class TogglingPagination(PageNumberPagination):

    def paginate_queryset(self, queryset, request, view=None):

        if 'no_page' in request.query_params:
            return None

        return super().paginate_queryset(queryset, request, view)

class FiftyResultsPagination(TogglingPagination):

    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50