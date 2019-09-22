from app import create_app,db
from app.models import *

from flask_script import Manager,Server,Shell
from flask_migrate import Migrate,MigrateCommand


app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
@manager.command
def test():
    import unittest
    test=unittest.TestLoader().discover('tests')
    unittest.TestRunner(verbosity=2).run(tests)

@manager.shell
def add_shell_context():
    return dict(app=app,db=db,User=User)

if __name__=='__main__':
    manager.run()