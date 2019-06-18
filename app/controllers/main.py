from flask import render_template, request, jsonify, redirect
from app import app
from app.controllers.noticias import noticias


n = noticias()

@app.route('/', methods=('GET', 'POST'))
def home():
    n.ultimas10()
    print(n.html)
    return render_template('Santander.html', html=n.html)

@app.route('/teste', methods=('GET', 'POST'))
def teste():
    n.ultimas10()
    print(n.html)
    return render_template('noticias.html', html=n.html)