from flask import Flask
from config import Config
from extensions import init_extensions
from blueprints.web import web_bp
from blueprints.api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

 # Cria as tabelas no banco (SQLite)
    with app.app_context():
        from models import Usuario, Sala, Reserva
        from extensions import db
        db.create_all()

    app.run(debug=True)