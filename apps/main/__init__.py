# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :        Liangz
   Date：          2018/11/8
-------------------------------------------------
   Change Activity:
                   2018/11/8:
-------------------------------------------------
"""


from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors
