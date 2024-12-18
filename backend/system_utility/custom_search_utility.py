from rest_framework.filters import SearchFilter


class CustomSearchFilter(SearchFilter):

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')

        if is_quoted_string(params):

            removed_quoted_char = params.replace('"', '')
            removed_quoted_char = removed_quoted_char.replace("'", '')
            return [removed_quoted_char]

        return params.split()


def is_quoted_string(value: str) -> bool:

    if len(value) > 0:

        single_quoted_string = value.startswith("'") and value.endswith("'")
        double_quoted_string = value.startswith('"') and value.endswith('"')

        return single_quoted_string or double_quoted_string

    return False