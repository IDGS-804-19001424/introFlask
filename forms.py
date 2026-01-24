from re import S
from wtforms import Form, IntegerField

from wtforms import StringField, PasswordField, EmailField, BooleanField
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
    