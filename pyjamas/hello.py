

# deps
from quart import Blueprint, render_template
from loguru import logger

bp = Blueprint('hello', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/static')


@bp.route('/')
async def hello_world():
    logger.info("Serving Hello World page.")
    return await render_template('hello.j2.html')
