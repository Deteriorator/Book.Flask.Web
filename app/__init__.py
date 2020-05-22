# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :        Liangz
   Date：          2018/11/8
-------------------------------------------------
   Change Activity:
                   2020/5/21:
-------------------------------------------------
"""
__author__ = 'Liangz'

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_script import Manager

# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)


# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])
#     config[config_name].init_app(app)
#
#     bootstrap.init_app(app)
#     mail.init_app(app)
#     moment.init_app(app)
#     db.init_app(app)
#
#     # from .main import main as main_blueprint
#     # app.register_blueprint(main_blueprint)
#     from .main import views
#     app.re
#
#     return app

# @app.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

#
# @app.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


from datetime import datetime


# @main.route('/')
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


if __name__ == '__main__':
    manager.run()
