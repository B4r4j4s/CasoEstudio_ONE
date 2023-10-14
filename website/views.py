from flask import Blueprint,render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Libro

views = Blueprint('views', __name__ )

@views.route('/')
def home():
    libros = Libro.query.limit(10).all()
    return render_template("home.html", user=current_user,libros=libros)

@views.route('/seguimiento')
def seguimiento():
    return render_template("seguimiento.html", user=current_user)

@views.route('/detalle_Libro/<int:id_libro>')
def detalle(id_libro):
    libro = Libro.query.get(id_libro)
    return render_template("detalle_libro.html", user=current_user,libro=libro)

@views.route('/carrito')
def carritoCompras():
    return render_template("pagos.html",user=current_user)

@views.route('/pagar', methods=['POST'])
def pagar():
    # Procesamiento del formulario
    return redirect(url_for('views.home'))

@views.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        # Ahora puedes usar 'titulo' para hacer una búsqueda en tu base de datos, por ejemplo.
        libros_encontrados = Libro.query.filter(Libro.titulo.ilike(f'%{titulo}%')).all()
        return render_template('buscar.html', user=current_user,libros=libros_encontrados)
    return render_template('home.html')

@views.route('/altas_libros')
def altas():
    return render_template('alta_libros.html',user=current_user)