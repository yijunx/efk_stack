from flask import current_app, Blueprint, render_template
admin = Blueprint('admin', __name__, url_prefix='')
from app_logger import logger

@admin.route('/')
def index():
    logger.info('helloworld hit')
    return {'hello': 'world'}