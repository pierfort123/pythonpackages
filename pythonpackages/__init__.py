from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid_redis_sessions import session_factory_from_settings
from pyramid.security import Allow
from pyramid.security import Authenticated
import os
import redis

auth_secret = os.getenv('AUTH_POLICY_SECRET', '')
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_secret = os.getenv('REDIS_SESSIONS_SECRET', '')
redis = redis.from_url(redis_url)


class UserFactory(object):
    @property
    def __acl__(self):
        return []


def main(global_config, **settings):
    """
    """
    authentication_policy = AuthTktAuthenticationPolicy(auth_secret)
    authorization_policy = ACLAuthorizationPolicy()
    settings['redis.sessions.secret'] = redis_secret
    settings['redis.sessions.url'] = redis_url
    session_factory = session_factory_from_settings(settings)
    config = Configurator(
        authentication_policy=authentication_policy,
        authorization_policy=authorization_policy,
        session_factory=session_factory,
        settings=settings,
        )
    config.add_route('about', '/about')
    config.add_view(
        'pythonpackages.views.about',
        route_name='about',
        renderer='pythonpackages:templates/about.mak')

    config.add_route('callback_github', '/callback_github')
    config.add_view(
        'pythonpackages.views.callback_github',
        route_name='callback_github')

    config.add_route('callback_pypi', '/callback_pypi')
    config.add_view(
        'pythonpackages.views.callback_pypi',
        route_name='callback_pypi')

    config.add_route('root', '/')
    config.add_view(
        'pythonpackages.views.root',
        route_name='root',
        renderer='pythonpackages:templates/root.mak')

    config.add_route('logout', '/logout')
    config.add_view(
        'pythonpackages.views.logout',
        route_name='logout')

    config.add_route('user', '/{user}',
        factory=UserFactory,
    )
    config.add_view(
        'pythonpackages.views.user',
        route_name='user',
        renderer='pythonpackages:templates/user.mak')

    config.add_static_view(
        'static', 'pythonpackages:static', cache_max_age=3600)

    config.include('pyramid_mako')
    config.include('pyramid_redis_sessions')

    return config.make_wsgi_app()
