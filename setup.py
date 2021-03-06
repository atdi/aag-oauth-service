from distutils.core import setup

setup(
    name='aag_oauth_service',
    version='0.0.1',
    packages=[''],
    url='',
    license='LGPL v3.0',
    author='aurel',
    author_email='aurel.avramescu@gmail.com',
    description='',
    install_requires=['tornado===4.0.2',
              'flask===0.10.1',
              'flask-oauthlib===0.7.0',
              'flask-sqlalchemy',
              'pyyaml',
              'sqlalchemy',
              'behave',
              'requests',
              'alembic',
              'pyhamcrest']
)
