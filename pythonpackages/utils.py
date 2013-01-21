

def get_query_string(request):
    """
        Return the query string if it exists in the request.
    """
    query_string = ''
    if 'QUERY_STRING' in request:
        query_string = request['QUERY_STRING']
    return query_string
