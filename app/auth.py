from flask import (
    Blueprint, 
    render_template,
    request,
    url_for,
    redirect,
    flash,
    session, 
    g
    )

# Para encriptar y comprobar la contraseña
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos los modelos para migrarlos a nuestra DB
from .models import User
from app import db

bp = Blueprint('auth', __name__, url_prefix = '/auth') #Ruta inicial a la que le añadimos las demas de abajo

@bp.route('/register', methods = ('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #Nos creamos nuestro user el que va a ser registrado en la DB con la psw encriptada
        user = User(username, generate_password_hash(password))

        error = None

        #Verificamos que no exista ese username con una query
        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya esta registrado'
        
        flash(error)
    
    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None

        # Validamos los datos
        user = User.query.filter_by(username=username).first()
        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta'

        #Iniciar sesion
        if error is None:
            session.clear()
            session['user_id'] = user.id

            return redirect(url_for('library.index'))
        
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# Evitar que se pueda  acceder a nuestra vista desde la url, que sea obligatorio hacer el login para verla
import functools
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view