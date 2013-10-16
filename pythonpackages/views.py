from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
from .utils import link_user
from . import redis
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import datetime
import os
import json
import requests


API_GH_USER = 'https://api.github.com/user?%s'

GH_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', '')
GH_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', '')

GH_AUTH = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GH_CLIENT_ID)

GH_ACCESS_TOKEN = 'https://github.com/login/oauth/access_token'

NOW = '%m/%d/%y'

PYPI_ACCESS_TOKEN = 'https://pypi.python.org/oauth/access_token'

payload = {
    'client_id': GH_CLIENT_ID,
    'client_secret': GH_CLIENT_SECRET,
    'code': None,
}
response = {
    'auth_url': GH_AUTH,
    'user': None,
}


def about(request):
    """
    """
    user = authenticated_userid(request)
    response['user'] = user
    return response


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
        payload['code'] = path_qs['/?code'][0]

        access_token = requests.post(
            GH_ACCESS_TOKEN, data=payload).content
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
    response['link_user'] = link_user
    response['logged_in'] = logged_in
    response['user'] = user
    return response


def user(request):
    """
    """
    user = request.path_qs.strip('/')
    if user in [i.decode() for i in redis.smembers('users')]:
        response['access_token'] = PYPI_ACCESS_TOKEN
        response['user'] = user
        return response
    else:
        raise(NotFound)
