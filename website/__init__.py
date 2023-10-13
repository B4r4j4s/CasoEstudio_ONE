from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
#DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # DATABASE LOCATION

    from .views import views #importar los files
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #registrar los blueprints
    app.register_blueprint(auth, url_prefix='/')
    return app