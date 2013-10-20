from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import has_permission
from pyramid.security import remember
from .config import auth_url
from .config import user_url
from .config import _now
from .config import client_id
from .config import GH_CLIENT_SECRET
from .config import GH_TOKEN_URL
from .config import PYPI_TOKEN_URL
from .db import db
from .utils import link_user
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import datetime
import json
import requests


def about(request):
    """
    """
    userid = authenticated_userid(request)
    return {
        'auth_url': auth_url,
        'user': userid,
    }


def activity(request):
    """
    """
    userid = authenticated_userid(request)
    logged_in = db.lrange('logged_in', 0, -1)
    return {
        'auth_url': auth_url,
        'link_user': link_user,
        'logged_in': logged_in,
        'user': userid,
    }


def callback_github(request):
    """
    Handle sign-ins; process callbacks from GitHub and log activity
    to database
    """
    path_qs = request.path_qs
    path_qs = urlparse.parse_qs(path_qs)
    if '/callback_github?code' in path_qs:

        payload = {
            'client_id': client_id,
            'client_secret': GH_CLIENT_SECRET,
            'code': path_qs['/callback_github?code'][0],
        }

        access_token = requests.post(
            GH_TOKEN_URL, data=payload).content
        access_token = access_token.decode()

        user_info = requests.get(user_url % access_token).content
        user_info = user_info.decode()
        user_info = json.loads(user_info)

        if 'login' in user_info:
            login = user_info['login']
        headers = remember(request, login)

        now = datetime.datetime.now()
        db.lpush(
            'logged_in', '%s logged in <%s>' % (login, now.strftime(_now)))
        db.sadd('users', login)

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
    return {
        'auth_url': auth_url,
        'link_user': link_user,
        'logged_in': logged_in,
        'user': userid,
    }


def user(request):
    """
    """
    path = request.path_qs.strip('/')
    if path in [i.decode() for i in db.smembers('users')]:
        userid = authenticated_userid(request)
        return {
            'access_token': PYPI_TOKEN_URL,
            'auth_url': auth_url,
            'has_permission': has_permission,
            'request': request,
            'path': path,
            'user': userid,
        }
    else:
        raise(NotFound)
