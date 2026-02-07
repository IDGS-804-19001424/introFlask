from re import S
from wtforms import Form, IntegerField

from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField, RadioField, SubmitField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Email", [
        validators.Email(message="Ingrese Correo Valido")
    ])


class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    cant_compradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message="Debe haber al menos 1 comprador")
    ])
    tarjeta = RadioField('Tarjeta Cineco', choices=[('Si', 'Si'), ('No', 'No')], default='No')
    cant_boletas = IntegerField('Cantidad de Boletas', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message="Debe comprar al menos 1 boleta")
    ])
    