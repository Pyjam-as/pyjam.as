from quart import Blueprint, render_template
from quart.static import send_from_directory
from loguru import logger

bp = Blueprint('hello', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/static')


@bp.route('/')
async def hello_world():
    logger.info("Serving Hello World page.")
    return await render_template('hello.j2.html')

@bp.route('/robots.txt')
async def robots():  # TODO:  🤖 as function name
    return await send_from_directory(bp.static_folder, "robots.txt")

@bp.route('/HA-GØH')
async def hagøh():
    logger.info("Serving HA-GØH page.")
    return await render_template('hag.j2.html')


@bp.route('/hackervandfald')
async def vandfald():
    logger.info("Serving hackervandfald page.")
    return await render_template('vandfald.j2.html')
