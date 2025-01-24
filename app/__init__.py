from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #Configuarcion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///MyLibraryList.db"
    )

    #Iniciar la DB con nuestra app
    db.init_app(app)

    # Anadimos nuestros BluePrints
    from . import library
    app.register_blueprint(library.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    #Pasar todos los modelos de nuestra app a la DB
    with app.app_context():
        db.create_all()

    return app
