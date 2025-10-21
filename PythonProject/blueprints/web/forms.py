from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, TimeField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=4)])
    confirmar = PasswordField("Confirmar Senha", validators=[
        DataRequired(), EqualTo("senha", message="As senhas devem ser iguais.")
    ])
    submit = SubmitField("Registrar")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class SalaForm(FlaskForm):
    nome = StringField("Nome da Sala", validators=[DataRequired()])
    capacidade = IntegerField("Capacidade")
    descricao = StringField("Descrição")
    submit = SubmitField("Salvar")


class ReservaForm(FlaskForm):
    sala_id = SelectField("Sala", coerce=int, validators=[DataRequired()])
    data = DateField("Data", validators=[DataRequired()])
    hora_inicio = TimeField("Hora de Início", validators=[DataRequired()])
    hora_fim = TimeField("Hora de Fim", validators=[DataRequired()])
    submit = SubmitField("Reservar")

