__author__ = 'aurel'


from aag_oauth_service import init_app, app

init_app()

if __name__ == '__main__':
    app.run()