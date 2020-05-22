# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :   程序路由
   Author :        Liangz
   Date：          2018/11/8
-------------------------------------------------
   Change Activity:
                   2018/11/8:
-------------------------------------------------
"""


from flask import render_template, session, redirect, url_for, current_app
# import apps
# from ..models import User
# from ..email import send_email
# from . import main
# from .forms import NameForm


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#             if current_app.config['FLASKY_ADMIN']:
#                 send_email(current_app.config['FLASKY_ADMIN'], 'New User',
#                            'mail/new_user', user=user)
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         return redirect(url_for('.index'))
#     return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


from datetime import datetime

# @main.route('/')
# @app.route('/')
# def index():
#     return render_template('index.html', current_time=datetime.utcnow())
