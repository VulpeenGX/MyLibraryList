from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    state = db.Column(db.Boolean, default = False)

    def __init__(self, created_by, title, author, genre, published_date, state = False):
        self.created_by = created_by
        self.title = title
        self.author = author
        self.genre = genre
        self.published_date = published_date
        self.state = state
    
    def __repr__(self):
        return f'<Libro: {self.title} by {self.author}>'
