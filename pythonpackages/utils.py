from urllib import parse


def get_query_string(request):
    """
    Return the parsed query string if it exists in the request.
    """
    qs = ''
    if 'QUERY_STRING' in request:
        qs = request['QUERY_STRING']
        qs = parse(qs)
    return qs
