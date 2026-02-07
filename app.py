import math
from flask import Flask, render_template, request
import forms
from forms import CinepolisForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# Configuración de la clave secreta (IMPORTANTE)
app.secret_key = 'clave_secreta_cinepolis'

# Inicializamos CSRF
csrf = CSRFProtect(app)

# --- RUTAS ---

@app.route('/')
def index():
    title = "IDGS804 -Intro Flask"
    listado = ['Juan', 'Ana', 'Pedro', 'Luisa'] 
    return render_template('index.html', title=title, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route("/hola")
def func():
    return 'Hola, Mundo --Hola!'

@app.route("/user/<string:user>")
def user(user):
    return f'Hola, {user}!'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Número: {n}<h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>¡Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default")
@app.route("/default/<string:parm>")
def func2(param="juan"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <label for="name">apaterno:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <input type="submit" value="Submit">
    </form>
    '''

@app.route("/operasBas", methods=['GET', 'POST'])
def operasbas():
    res = None
    if request.method == 'POST':          
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        operacion = request.form.get('operacion')

        # Convertimos a float asegurándonos de que existen
        if n1 and n2:
            n1 = float(n1)
            n2 = float(n2)
            
            if operacion == 'sumar':
                res = n1 + n2
            elif operacion == 'restar':
                res = n1 - n2
            elif operacion == 'multiplicar':
                res = n1 * n2
            elif operacion == 'dividir':
                res = n1 / n2
          
    return render_template('operasBas.html', res=res)

# --- AQUI ESTABA TU ERROR: Borré la segunda 'app = Flask(__name__)' que tenías aquí ---

@app.route('/distancia', methods=['GET', 'POST'])
def calcular_distancia():
    resultado = None
    if request.method == 'POST':
        try:
            x1 = float(request.form['x1'])
            y1 = float(request.form['y1'])
            x2 = float(request.form['x2'])
            y2 = float(request.form['y2'])
            
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            resultado = round(distancia, 2)
            
        except ValueError:
            resultado = "Error: Por favor ingresa solo números válidos."

    return render_template('distancia.html', resultado=resultado)

@app.route("/alumnos", methods =["GET", "POST"])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_class = forms.UserForm(request.form)
    if request.method=='POST' and alumno_class.validate():
        mat = alumno_class.matricula.data
        nom = alumno_class.nombre.data
        ape = alumno_class.apellido.data
        email = alumno_class.correo.data
    return render_template("alumnos.html", form=alumno_class, mat=mat, nom=nom, ape=ape, email=email)

@app.route("/cinepolis", methods=['GET', 'POST'])
def cinepolis():
    form = CinepolisForm(request.form)
    total_pagar = 0.0
    mensaje = ""

    if request.method == 'POST' and form.validate():
        try:
            nombre = form.nombre.data
            compradores = int(form.cant_compradores.data)
            boletas = int(form.cant_boletas.data)
            tarjeta = form.tarjeta.data
            
            max_boletas_permitidas = compradores * 7

            if boletas > max_boletas_permitidas:
                mensaje = f"Error: No se pueden comprar más de 7 boletas por persona. (Máximo permitido para {compradores} personas: {max_boletas_permitidas})"
            else:
                precio_unitario = 12000
                total = boletas * precio_unitario

                if boletas > 5:
                    total = total * 0.85 
                elif boletas >= 3:
                    total = total * 0.90 

                if tarjeta == 'Si':
                    total = total * 0.90 
                
                total_pagar = total
                mensaje = f"Procesado exitosamente para {nombre}"

        except Exception as e:
            mensaje = "Ocurrió un error en el cálculo"

    return render_template("cinepolis.html", form=form, total=total_pagar, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)