from flask import Flask, render_template, request
from datetime import datetime
import equilibrium
from lexer import Lexer
from parserr import Parser


app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
	code = request.form['code'].replace('\r','').split('\n')

	lexer = Lexer(code)
	parser = Parser()

	parser.parser(lexer.lexer())

	if parser.web_output:
		return render_template('index.html',web_output='\n'.join(parser.web_output))
	else:
		return render_template('index.html')

@app.route('/api')
def api():
	return 'API :)'

if __name__ == "__main__":
    app.run(debug=True)
