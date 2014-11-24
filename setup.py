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
    requires=['tornado',
              'python-oauth2',
              'sqlalchemy',
              'behave',
              'requests',
              'alembic',
              'pyhamcrest']
)
