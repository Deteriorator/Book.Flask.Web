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

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_script import Manager
from apps.main.forms import NameForm

# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# db = SQLAlchemy(app)
mail = Mail(app)

# def create_app(config_name):
#     apps = Flask(__name__)
#     apps.config.from_object(config[config_name])
#     config[config_name].init_app(apps)
#
#     bootstrap.init_app(apps)
#     mail.init_app(apps)
#     moment.init_app(apps)
#     db.init_app(apps)
#
#     # from .main import main as main_blueprint
#     # apps.register_blueprint(main_blueprint)
#     from .main import views
#     apps.re
#
#     return apps

# @apps.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

#
# @apps.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


from datetime import datetime


# @main.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if (old_name is not None) and (old_name != form.name.data):
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        current_time=datetime.utcnow()
    )


if __name__ == '__main__':
    manager.run()
