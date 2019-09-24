
from quart import Quart
from loguru import logger


def create_app():
    """ Factory function
    Returns Quart app object """
    logger.info("Starting pyjam.as!")
    app = Quart(__name__)

    from . import hello
    app.register_blueprint(hello.bp)

    return app
