from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse
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
    """

def logout(request):
    """
    Forget user
    """
    userid = authenticated_userid(request)
    headers = forget(request)
    utils.logged_out(userid)
    return HTTPFound(location="/", headers=headers)
