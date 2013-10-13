from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import os
import requests


GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', '')
GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', '')
GITHUB_URL_AUTH = 'https://github.com/login/oauth/authorize?client_id=%s'
GITHUB_URL_AUTH_TOKEN = 'https://github.com/login/oauth/access_token'
GITHUB_URL_USER = 'https://api.github.com/user?%s'


def about(request):
    return {}


def contact(request):
    return {}


def login(request):
    """
    """
    query_string = None
    if 'QUERY_STRING' in request:
        query_string = request['QUERY_STRING']
    query_string = urlparse.parse_qs(query_string)
    if query_string:
        if 'code' in query_string:
            code = query_string['code']
            payload = {
                'client_id': GITHUB_CLIENT_ID,
                'client_secret': GITHUB_CLIENT_SECRET,
                'code': code,
            }
            access_token = requests.post(
                GITHUB_URL_AUTH_TOKEN, data=payload).content
            access_token = requests.get(
                GITHUB_URL_USER % access_token).content
            headers = remember(request, userid)
            return HTTPFound(location="/", headers=headers)
    else:
        HTTPFound(location=GITHUB_URL_AUTH % GITHUB_CLIENT_ID)

    return {}

def logout(request):
    """
    """
    headers = forget(request)
    return HTTPFound(location="/", headers=headers)
