from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import has_permission
from pyramid.security import remember
from .config import _now

from .config import GITHUB_AUTH_URL
from .config import auth_url_pypi

from .config import GITHUB_CLIENT_ID
from .config import GITHUB_CLIENT_SECRET

from .config import client_id_pypi
from .config import client_secret_pypi

from .config import token_url_gh
from .config import token_url_pypi

from .config import user_url

from .db import db
from .utils import link_user
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
import datetime
import json
import requests
import requests_oauthlib


def about(request):
    """
    """
    userid = authenticated_userid(request)
    return {
        'auth_url': GITHUB_AUTH_URL,
        'user': userid,
    }


def activity(request):
    """
    """
    userid = authenticated_userid(request)
    logged_in = db.lrange('logged_in', 0, -1)
    return {
        'auth_url': GITHUB_AUTH_URL,
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
            'client_id': GITHUB_CLIENT_ID,
            'client_secret': GITHUB_CLIENT_SECRET,
            'code': path_qs['/callback_github?code'][0],
        }

        access_token = requests.post(
            token_url_gh, data=payload).content
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


def callback_pypi(request):
    """
    Thanks to Richard Jones for this PyPI OAuth code
    """
    auth = requests_oauthlib.OAuth1(
        client_id_pypi,
        client_secret_pypi,
        signature_type='auth_header')
    response = requests.get(token_url_pypi, auth=auth, verify=False)
    query_string = urlparse.parse_qs(response.content)
    if 'oauth_token_secret' in query_string:
        oauth_token_secret = query_string['oauth_token_secret'][0]
    if 'oauth_token' in query_string:
        oauth_token = query_string['oauth_token'][0]
    return HTTPFound(
        location=auth_url_pypi % query_string)


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
        'auth_url': GITHUB_AUTH_URL,
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
            'access_token': token_url_pypi,
            'auth_url': GITHUB_AUTH_URL,
            'has_permission': has_permission,
            'request': request,
            'path': path,
            'user': userid,
        }
    else:
        raise(NotFound)
