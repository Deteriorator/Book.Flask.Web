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
import os

# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=1)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False),
        current_time=datetime.utcnow()
    )


if __name__ == '__main__':
    manager.run()
