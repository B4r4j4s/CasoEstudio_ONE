from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'

    from .views import views #importar los files
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #registrar los blueprints
    app.register_blueprint(auth, url_prefix='/')
    return app