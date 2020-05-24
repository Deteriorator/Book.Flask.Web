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

from flask import render_template, redirect, request, url_for, flash
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
