from pyramid.config import Configurator


def main(global_config, **settings):
    """
    """
    config = Configurator()
    return config.make_wsgi_app()
