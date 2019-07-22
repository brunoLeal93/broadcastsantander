from flask import render_template, request, jsonify, redirect
from app import app
from app.controllers.noticias import noticias


@app.route('/', methods=('GET', 'POST'))
def home():

    return render_template('Santander.html')

@app.route('/teste', methods=('GET', 'POST'))
def teste():
    n = noticias()
    n.ultimas10()
    
    return render_template('noticias.html', html=n.html)