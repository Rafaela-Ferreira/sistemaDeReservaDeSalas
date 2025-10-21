from flask import jsonify
from . import api_bp
from models import Usuario

@api_bp.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios])
