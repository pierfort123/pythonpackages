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
GITHUB_URL_AUTH = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GITHUB_CLIENT_ID)
GITHUB_URL_AUTH_TOKEN = 'https://github.com/login/oauth/access_token'
GITHUB_URL_USER = 'https://api.github.com/user?%s'


def about(request):
    return {}


def contact(request):
    return {}


def login(request):
    """
    """
    path_qs = request.path_qs
    path_qs = urlparse.parse_qs(path_qs)
    if path_qs:
        if 'code' in path_qs:
            code = path_qs['code']
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
        HTTPFound(location=GITHUB_URL_AUTH) 

    return {
        'userid': userid,
    }

def logout(request):
    """
    """
    headers = forget(request)
    return HTTPFound(location="/", headers=headers)


def root(request):
    """
    """
    return {
        'auth_url': GITHUB_URL_AUTH,
    }
