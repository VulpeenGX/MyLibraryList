from flask import Blueprint, render_template, request, redirect, url_for, g
from .auth import login_required
from .models import Libro, User
from . import db
from datetime import datetime


bp = Blueprint('library', __name__, url_prefix = '/library') #Ruta inicial a la que le añadimos las demas de abajo


@bp.route('/list') #Rutas secundarias 
@login_required
def index():
    libros = Libro.query.all()
    return render_template('/library/index.html', libros = libros)


# Añadir libros
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        published_date_str = request.form['published_date']
        state = request.form['state'] == 'true'

        # Pasamos el date de string a objeto date
        published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()

        libro = Libro(
            created_by=g.user.id, 
            title=title, 
            author=author, 
            genre=genre, 
            published_date=published_date, 
            state=state  
        )

        db.session.add(libro)
        db.session.commit()

        return redirect(url_for('library.index'))

    return render_template('library/create.html')

# para cargar libros en varibles 
def get_libro(id):
    libro = Libro.query.get_or_404(id)
    return libro

#Editar libros
@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    
    libro = get_libro(id)

    if request.method == 'POST':
        libro.title = request.form['title']
        libro.author = request.form['author']
        libro.genre = request.form['genre']
        published_date_str = request.form['published_date']
        libro.state = request.form['state'] == 'true'

        # Pasamos el date de string a objeto date
        libro.published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()

        db.session.commit()
        return redirect(url_for('library.index'))

    return render_template('library/update.html', libro = libro)

#Eliminar libros
@bp.route('/delete/<int:id>', methods=('POST',)) 
@login_required
def delete(id):
    libro = get_libro(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('library.index'))
