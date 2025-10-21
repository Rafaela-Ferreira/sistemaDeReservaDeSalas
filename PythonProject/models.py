from extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    reservas = db.relationship("Reserva", backref="usuario", lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    capacidade = db.Column(db.Integer)
    descricao = db.Column(db.String(255))
    reservas = db.relationship("Reserva", backref="sala", lazy=True)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey("sala.id"), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)