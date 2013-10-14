from pyramid.config import Configurator
from .store import redis


def main(global_config, **settings):
    """
    """
    config = Configurator()

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

    return config.make_wsgi_app()
