from flask import render_template, redirect, url_for, flash, request
from . import web_bp
from .forms import LoginForm, RegistroForm, SalaForm, ReservaForm
from extensions import db
from models import Usuario, Sala, Reserva
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime

@web_bp.route("/")
def index():
    return render_template("lista.html")

@web_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.senha == form.senha.data:
            login_user(usuario)
            return redirect(url_for("web.index"))
        flash("Credenciais inválidas.")
    return render_template("login.html", form=form)

@web_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("web.login"))

@web_bp.route("/registro", methods=["GET", "POST"])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        novo = Usuario(nome=form.nome.data, email=form.email.data, senha=form.senha.data)
        db.session.add(novo)
        db.session.commit()
        flash("Usuário registrado com sucesso!")
        return redirect(url_for("web.login"))
    return render_template("registro.html", form=form)

@web_bp.route("/salas", methods=["GET", "POST"])
@login_required
def cadastrar_sala():
    form = SalaForm()
    if form.validate_on_submit():
        sala = Sala(nome=form.nome.data, capacidade=form.capacidade.data, descricao=form.descricao.data)
        db.session.add(sala)
        db.session.commit()
        flash("Sala cadastrada com sucesso!")
        return redirect(url_for("web.lista_salas"))
    return render_template("cadastrar_sala.html", form=form)

@web_bp.route("/salas/lista")
@login_required
def lista_salas():
    salas = Sala.query.all()
    return render_template("lista.html", salas=salas)

@web_bp.route("/reservar", methods=["GET", "POST"])
@login_required
def reservar():
    form = ReservaForm()
    form.sala_id.choices = [(s.id, s.nome) for s in Sala.query.all()]

    if form.validate_on_submit():
        reserva = Reserva(
            usuario_id=current_user.id,
            sala_id=form.sala_id.data,
            data=form.data.data,
            hora_inicio=form.hora_inicio.data,
            hora_fim=form.hora_fim.data
        )
        db.session.add(reserva)
        db.session.commit()
        flash("Reserva feita com sucesso!")
        return redirect(url_for("web.index"))
    return render_template("reservar.html", form=form)

@web_bp.route("/reservas/lista")
@login_required
def lista_reservas():
    reservas = Reserva.query.all()
    return render_template("lista_reservas.html", reservas=reservas)

@web_bp.route("/salas/editar/<int:sala_id>", methods=["GET", "POST"])
@login_required
def editar_sala(sala_id):
    sala = Sala.query.get_or_404(sala_id)
    form = SalaForm(obj=sala)
    if form.validate_on_submit():
        sala.nome = form.nome.data
        sala.capacidade = form.capacidade.data
        sala.descricao = form.descricao.data
        db.session.commit()
        flash("Sala atualizada com sucesso!")
        return redirect(url_for("web.lista_salas"))
    return render_template("cadastrar_sala.html", form=form)

@web_bp.route("/salas/excluir/<int:sala_id>")
@login_required
def excluir_sala(sala_id):
    sala = Sala.query.get_or_404(sala_id)
    db.session.delete(sala)
    db.session.commit()
    flash("Sala excluída com sucesso!")
    return redirect(url_for("web.lista_salas"))