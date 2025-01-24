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
