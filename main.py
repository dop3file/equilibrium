from flask import Flask, render_template, url_for, request, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import equilibrium


app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
	if request.method == 'POST':
		code = request.form['code'].split('\n')
		Eq = equilibrium.Equilibrium(code,'DEBUG')
		Eq.run_code()
		return render_template('index.html')
	else:
		return render_template('index.html')
		flash('Succes!')	

if __name__ == "__main__":
    app.run(debug=False)
