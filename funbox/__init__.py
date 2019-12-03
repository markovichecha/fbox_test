import configparser

from flask import Flask

from funbox import utils
from funbox import db
from funbox import api


def create_app(testing=False):
    app = Flask(__name__)
    config = configparser.ConfigParser()
    config.read('main.ini')
    redis_db_inst = config.get('REDIS', 'TEST_INSTANCE') if testing else config.get('REDIS', 'PROD_INSTANCE')
    app.config['DATABASE'] = db.set_pool(host=config.get('REDIS', 'HOST'), db=redis_db_inst)
    app.register_blueprint(api.bp)

    return app
