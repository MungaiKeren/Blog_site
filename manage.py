from app import create_app
# from app.models import *
from flask_script import Manager,Server


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    import unittest
    test=unittest.TestLoader().discover('tests')
    unittest.TestRunner(verbosity=2).run(tests)

if __name__=='__main__':
    manager.run