from . import config
from . import utils


def login(request):
    """
        Do OAUTH dance with GitHub (for sign in) and PyPI (for releasing
        packages)
    """
#    # Redir https
#    if request.headers.get('X-Forwarded-Proto') is not None:
#        if request.headers['X-Forwarded-Proto'] != 'https':
#            return HTTPMovedPermanently(location="https://%s%s" % (
#                request.host, request.path_qs))
    betacount = utils.get_beta_count()
    code = None
    followers = utils.get_followers()
    fortune = utils.get_fortune()
    num_downloads, num_packages, num_packages_pypi, num_times_featured = \
        utils.get_numbers()
    userid = authenticated_userid(request)
    qs = utils.get_query_string(request)
    qs = urlparse.parse_qs(qs)
    # PyPI OAuth, not used for login
    if 'oauth_token' in qs:
        auth = requests.auth.OAuth1(config.PYPI_OAUTH_CONSUMER_KEY,
            config.PYPI_OAUTH_CONSUMER_SECRET,
            unicode(utils.db.get(config.REDIS_KEY_USER_PYPI_OAUTH_TOKEN %
                userid)),
            unicode(utils.db.get(config.REDIS_KEY_USER_PYPI_OAUTH_SECRET %
                userid)),
            signature_type='auth_header')
        response = requests.get(config.PYPI_URL_OAUTH_ACCESS_TOKEN, auth=auth,
            verify=False)
        response = urlparse.parse_qs(response.content)
        utils.db.set(config.REDIS_KEY_USER_PYPI_OAUTH_SECRET % userid,
            unicode(response['oauth_token_secret'][0]))
        utils.db.set(config.REDIS_KEY_USER_PYPI_OAUTH_TOKEN % userid,
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
    recent_users = dict()
    return {
        'betacount': betacount,
        'followers': followers,
        'fortune': fortune,
        'github_auth': config.GITHUB_URL_AUTH,
        'menu': menu,
        'headers': headers,
        'num_downloads': num_downloads,
        'num_packages': num_packages,
        'num_packages_pypi': num_packages_pypi,
        'num_times_featured': num_times_featured,
        'recent_users': recent_users,
        'userid': userid,
    }


def logout(request):
    """
        Forget user
    """
#    # Redir https
#    if request.headers.get('X-Forwarded-Proto') is not None:
#        if request.headers['X-Forwarded-Proto'] != 'https':
#            return HTTPMovedPermanently(location="https://%s%s" % (
#                request.host, request.path_qs))
    userid = authenticated_userid(request)
    headers = forget(request)
    utils.logged_out(userid)
    return HTTPFound(location="/", headers=headers)

