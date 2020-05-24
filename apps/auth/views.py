#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    views.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.24   15:32
-------------------------------------------------------------------------------
   @Change:   2020.05.24
-------------------------------------------------------------------------------
"""

from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')

