

# deps
from quart import Blueprint
from loguru import logger

bp = Blueprint('hello', __name__)


@bp.route('/')
def hello_world():
    logger.info("Serving Hello World page.")
    return "Hello, world!"
