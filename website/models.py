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
    direccion = db.Column(db.String(150)) 
    notes = db.relationship('Note')

#Libros
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), unique=True)
    autor =  db.Column(db.String(150))
    ISBN =  db.Column(db.String(150))
    desc =  db.Column(db.String(150))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)

#Pedidos
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'))
    cant = db.Column(db.Integer)
    estado = db.Column(db.String(150))
    paqueteria_id = db.Column(db.Integer, db.ForeignKey('paqueteria.id'))
    precio_libro = db.Column(db.Integer)
    precio_envio = db.Column(db.Integer)

#Paqueteria
class Paqueteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_paqueteria = db.Column(db.String(150))
    tarifa = db.Column(db.Integer)

#Proveedor
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_proveedor = db.Column(db.String(150))
    dir_proveedor = db.Column(db.String(150)) 
    email_proveedor = db.Column(db.String(150), unique=True)
    
    