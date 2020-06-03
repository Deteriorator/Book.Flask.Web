#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    decorators.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.06.03   9:13
-------------------------------------------------------------------------------
   @Change:   2020.06.03
-------------------------------------------------------------------------------
"""

from functools import wraps
from flask import g
from .errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator


