# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     manage
   Description :   用于启动程序以及其他的程序任务
   Author :        Liangz
   Date：          2018/11/8
-------------------------------------------------
   Change Activity:
                   2018/11/8:
-------------------------------------------------
"""
__author__ = 'Liangz'


import os
# from apps import create_app, db
from apps import app #, db
# from apps.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


# apps = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app) #, db)
app.config['DEBUG'] = True

def make_shell_context():
    return dict(app=app) #, db=db, User=User, Role=Role)
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
