import math
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'clave secreta'


@app.route('/')
def index():
    title = "IDGS804 -Intro Flask"
    listado =['Juan', 'Ana', 'Pedro', 'Luisa'] 

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
def username(id,username):
    return f"<h1>¡Hola, {username}! Tu ID es: {id}"


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"


@app.route("/default")
@app.route("/default/<string:parm>")
def func2(param="juan"):
    return f"<h1>¡Hola, {param}!</h1>"


app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name>Name:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <label for="name">apaterno:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <input type="submit" value="Submit">
    </form>
    '''

@app.route("/OperasBas,")
def OperasBas():
    return render_template("operasBas.html")


@app.route("/operasBas", methods=['GET', 'POST'])
def operasbas():
        res = None
        if request.method == 'POST':           
          n1=request.form.get('num1')
          n2=request.form.get('num2')

          if request.form.get('operacion')=='sumar':
              res=float(n1)+float(n2)
          if request.form.get('operacion')=='restar':
              res=float(n1)-float(n2)
          if request.form.get('operacion')=='multiplicar':
              res=float(n1)*float(n2)
          if request.form.get('operacion')=='dividir':
              res=float(n1)/float(n2)
          
        return render_template('operasBas.html', res=res,)

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)