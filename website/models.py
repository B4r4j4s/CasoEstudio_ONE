from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): #ejemplo
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Recopila la fecha automaticamente
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Conectar dos tablas 

class User(db.Model, UserMixin): #Definir las tablas de usuario, practicamente lo mismo que tenemos en sql
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

#Libros
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), unique=True)
    categoria = db.Column(db.String(150))
    precio = db.Column(db.Integer)

#Ordenes