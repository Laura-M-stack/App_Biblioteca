
from flask import Flask, render_template
import biblioteca
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    libros = []
    try:
        with open('libros.json', 'r') as f:
            libros = json.load(f)
    except FileNotFoundError:
        libros = []
    socios = []
    try:
        with open('socios.json', 'r') as f:
            socios = json.load(f)
    except FileNotFoundError:
        socios = []
    prestamos = []
    try:
        with open('prestamos.json', 'r') as f:
            prestamos = json.load(f)
    except FileNotFoundError:
        prestamos = []

    return render_template('index.html', libros=libros, socios=socios, prestamos=prestamos)

if __name__ == '__main__':
    app.run(debug=True)