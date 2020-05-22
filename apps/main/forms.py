# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :
   Author :        Liangz
   Date：          2018/11/8
-------------------------------------------------
   Change Activity:
                   2018/11/8:
-------------------------------------------------
"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    # 新版本
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
