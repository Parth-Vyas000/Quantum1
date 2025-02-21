from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/quantum_crypto'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
