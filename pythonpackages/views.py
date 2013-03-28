from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
from urllib import parse as urlparse
from . import config
from . import utils
import json
import requests


def about(request):
    return {}


def contact(request):
    return {}


def login(request):
    """
    Do OAuth: with GitHub for sign in, and PyPI for package releasing.
    """
    code = None
    qs = utils.get_query_string(request)
    userid = authenticated_userid(request)

    # PyPI OAuth, not used for sign in
    if 'oauth_token' in qs:
        auth = requests.auth.OAuth1(
            config.PYPI_OAUTH_CONSUMER_KEY,
            config.PYPI_OAUTH_CONSUMER_SECRET,
            unicode(
                utils.db.get(
                    config.REDIS_KEY_USER_PYPI_OAUTH_TOKEN %
                    userid)),
            unicode(
                utils.db.get(
                    config.REDIS_KEY_USER_PYPI_OAUTH_SECRET %
                    userid)),
            signature_type='auth_header')
        response = requests.get(
            config.PYPI_URL_OAUTH_ACCESS_TOKEN, auth=auth,
            verify=False)
        response = urlparse.parse_qs(response.content)
        utils.db.set(
            config.REDIS_KEY_USER_PYPI_OAUTH_SECRET % userid,
            unicode(response['oauth_token_secret'][0]))
        utils.db.set(
            config.REDIS_KEY_USER_PYPI_OAUTH_TOKEN % userid,
            unicode(response['oauth_token'][0]))
        return HTTPFound(location="/manage/account/pypi")
    if userid is not None:
        return HTTPFound(location="/dashboard")
    else:
        menu = utils.no_sign_in()
    headers = None
    userinfo = None
    if 'code' in qs:
        code = qs['code']
        token = utils.get_access_token(code)
        userinfo = utils.get_user_info(token)
        userinfo = json.loads(userinfo)
        avatar, email, name, userid = utils.get_user_id(userinfo)
        utils.set_avatar(userid, avatar)
        utils.set_email(userid, email)
        utils.set_name(userid, name)
        if not utils.db.exists(config.REDIS_KEY_USER_PLAN % userid):
            utils.set_plan(userid, 'free')
        utils.set_token(userid, token)
        utils.set_slots(userid)
        headers = remember(request, userid)
        utils.set_logged_in(userid)
        return HTTPFound(location="/dashboard", headers=headers)
    return {
        'github_auth': config.GITHUB_URL_AUTH,
        'menu': menu,
        'headers': headers,
        'userid': userid,
    }


def logout(request):
    """
    Forget user
    """
    userid = authenticated_userid(request)
    headers = forget(request)
    utils.logged_out(userid)
    return HTTPFound(location="/", headers=headers)
