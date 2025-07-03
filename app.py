from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    datos = {
        'fecha': request.form['fecha'],
        'nombre': request.form['nombre'],
        'correo': request.form['correo'],
        'equipo': request.form['equipo'],
        'reparacion': request.form['reparacion'],
        'medio': request.form['medio'],
        'telefono': request.form['telefono'],
        'estatus': request.form['estatus'],
        'pin': request.form['pin']
    }
    return render_template('resultado.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
