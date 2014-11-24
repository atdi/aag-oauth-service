from distutils.core import setup

setup(
    name='aag-oauth-service',
    version='0.0.1',
    packages=[''],
    url='',
    license='LGPL v3.0',
    author='aurel',
    author_email='aurel.avramescu@gmail.com',
    description='',
    requires=['tornado===4.0.2',
              'flask===0.10.1',
              'flask-oauthlib===0.7.0',
              'flask-sqlalchemy',
              'sqlalchemy',
              'behave',
              'requests',
              'alembic',
              'pyhamcrest']
)
