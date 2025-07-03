from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    return f"<h2>Usuario ingresado: {usuario}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
