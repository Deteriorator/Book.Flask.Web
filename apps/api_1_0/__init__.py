#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    __init__.py.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.06.03   9:01
-------------------------------------------------------------------------------
   @Change:   2020.06.03
-------------------------------------------------------------------------------
"""

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors

