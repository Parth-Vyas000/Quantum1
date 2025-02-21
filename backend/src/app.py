from flask import Flask
from src.config.db_config import db, init_app
from src.routes.auth_routes import auth_blueprint

app = Flask(__name__)
init_app(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
