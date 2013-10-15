from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import os
import json
import requests


API_GH_USER = 'https://api.github.com/user?%s'

GH_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', '')
GH_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', '')

GH_LOGIN_AUTH = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GH_CLIENT_ID)

GH_LOGIN_TOKEN = 'https://github.com/login/oauth/access_token'


def logout(request):
    """
    """
    headers = forget(request)
    return HTTPFound(location="/", headers=headers)


def root(request):
    """
    """
    access_token, code, user_info = None, None, None
    user = authenticated_userid(request)
    path_qs = request.path_qs
    path_qs = urlparse.parse_qs(path_qs)
    if '/?code' in path_qs:
        code = path_qs['/?code'][0]
        payload = {
            'client_id': GH_CLIENT_ID,
            'client_secret': GH_CLIENT_SECRET,
            'code': code,
        }
        access_token = requests.post(
            GH_LOGIN_TOKEN, data=payload).content
        access_token = access_token.decode()
        user_info = requests.get(
            API_GH_USER % access_token).content
        login = json.loads(user_info)['login']
        headers = remember(request, login)
        return HTTPFound(location="/", headers=headers)
    return {
        'user': user,
        'auth_url': GH_LOGIN_AUTH,
    }
