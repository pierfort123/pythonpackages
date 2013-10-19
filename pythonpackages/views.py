from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.security import Allow
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import has_permission
from pyramid.security import remember
from .db import db
from .utils import link_user
from . import UserFactory
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import datetime
import os
import json
import requests


API_GH_USER = 'https://api.github.com/user?%s'

FORMAT = '%m/%d/%y'

GH_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', '')
GH_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', '')

GH_AUTH_URL = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GH_CLIENT_ID)

GH_TOKEN_URL = 'https://github.com/login/oauth/access_token'

PYPI_TOKEN_URL = 'https://pypi.python.org/oauth/access_token'

payload = {
    'client_id': GH_CLIENT_ID,
    'client_secret': GH_CLIENT_SECRET,
    'code': None,
}
response = {
    'auth_url': GH_AUTH_URL,
    'user': None,
}


def about(request):
    """
    """
    userid = authenticated_userid(request)
    response['user'] = userid
    return response


def callback_github(request):
    """
    Handle sign-ins; process callbacks from GitHub and log activity
    to database
    """

    user_factory = UserFactory(request)

    path_qs = request.path_qs
    path_qs = urlparse.parse_qs(path_qs)
    if '/callback_github?code' in path_qs:
        payload['code'] = path_qs['/callback_github?code'][0]

        access_token = requests.post(
            GH_TOKEN_URL, data=payload).content
        access_token = access_token.decode()

        user_info = requests.get(
            API_GH_USER % access_token).content
        user_info = user_info.decode()
        user_info = json.loads(user_info)

        if 'login' in user_info:
            login = user_info['login']
        headers = remember(request, login)

        now = datetime.datetime.now()
        db.lpush(
            'logged_in', '%s logged in <%s>' % (login, now.strftime(FORMAT)))
        db.sadd('users', login)

        user_factory.__acl__.append(Allow, login, 'manage')

        return HTTPFound(location="/%s" % login, headers=headers)
    raise(NotFound)  # No query string, nothing to see here


def callback_pypi():
    """
    """


def logout(request):
    """
    Trigger authtkt machinery to forget current user
    """
    headers = forget(request)
    return HTTPFound(location="/", headers=headers)


def root(request):
    """
    """
    userid = authenticated_userid(request)
    logged_in = db.lrange('logged_in', 0, 4)
    response['link_user'] = link_user
    response['logged_in'] = logged_in
    response['user'] = userid
    return response


def user(request):
    """
    """
    userid = request.path_qs.strip('/')
    if userid in [i.decode() for i in db.smembers('users')]:
        response['access_token'] = PYPI_TOKEN_URL
        response['has_permission'] = has_permission
        response['request'] = request
        response['user'] = userid
        return response
    else:
        raise(NotFound)
