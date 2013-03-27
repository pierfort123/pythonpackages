from pyramid.config import Configurator


def root(request):
    """
    """
    return {}


def main(global_config, **settings):
    """
    """
    config = Configurator()

    config.add_route('root', '/')
    config.add_view(root, route_name='root',
         renderer='pythonpackages:templates/root.mak')

    config.add_route('about', '/about')
    config.add_view('pythonpackages.views.about',
        route_name='about',
        renderer='pythonpackages:templates/about.mak')

    config.add_route('login', '/login')
    config.add_view('pythonpackages.views.login', route_name='login',
         renderer='pythonpackages:templates/login.mak')

    return config.make_wsgi_app()
