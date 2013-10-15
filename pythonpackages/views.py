from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import datetime
import os
import json
import requests
from . import redis


API_GH_USER = 'https://api.github.com/user?%s'

GH_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', '')
GH_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', '')

GH_LOGIN_AUTH = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GH_CLIENT_ID)

GH_LOGIN_TOKEN = 'https://github.com/login/oauth/access_token'

NOW = '%m/%d/%y'

PAYLOAD = {
    'client_id': GH_CLIENT_ID,
    'client_secret': GH_CLIENT_SECRET,
    'code': None,
}

RESPONSE = {
    'auth_url': GH_LOGIN_AUTH,
    'user': None,
}


def about(request):
    """
    """
    user = authenticated_userid(request)
    RESPONSE['user'] = user
    return RESPONSE


def logout(request):
    """
    Trigger authtkt machinery to forget current user 
    """
    headers = forget(request)
    return HTTPFound(location="/", headers=headers)


def root(request):
    """
    Handle sign-ins; process callbacks from GitHub and log activity
    to database
    """
    user = authenticated_userid(request)
    logged_in = redis.lrange('logged_in', 0, 4)
    path_qs = request.path_qs
    path_qs = urlparse.parse_qs(path_qs)
    if '/?code' in path_qs:
        PAYLOAD['code'] = path_qs['/?code'][0]

        access_token = requests.post(
            GH_LOGIN_TOKEN, data=PAYLOAD).content
        access_token = access_token.decode()

        user_info = requests.get(
            API_GH_USER % access_token).content
        user_info = user_info.decode()
        user_info = json.loads(user_info)

        if 'login' in user_info:
            login = user_info['login']
        headers = remember(request, login)

        now = datetime.datetime.now()
        redis.lpush(
            'logged_in', '%s logged in <%s>' % (login, now.strftime(NOW)))
        redis.sadd('users', login)

        return HTTPFound(location="/", headers=headers)
    RESPONSE['logged_in'] = logged_in
    RESPONSE['user'] = user
    return RESPONSE


def user(request):
    """
    """
    user = authenticated_userid(request)
    RESPONSE['user'] = user
    return RESPONSE
