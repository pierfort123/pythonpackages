from pyramid.config import Configurator
import os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_secret = os.getenv('REDIS_SESSIONS_SECRET', '')
redis = redis.from_url(redis_url)


def main(global_config, **settings):
    """
    """

    settings['redis.sessions.secret'] = redis_secret
    settings['redis.sessions.url'] = redis_url
    config = Configurator(settings=settings)

    config.add_route('root', '/')
    config.add_view(
        'pythonpackages.views.root',
        route_name='root',
        renderer='pythonpackages:templates/root.mak')

    config.add_route('logout', '/logout')
    config.add_view(
        'pythonpackages.views.logout',
        route_name='logout',
        renderer='pythonpackages:templates/logout.mak')

    config.add_static_view(
        'static', 'pythonpackages:static', cache_max_age=3600)

    config.include('pyramid_mako')
    config.include('pyramid_redis_sessions')

    return config.make_wsgi_app()
