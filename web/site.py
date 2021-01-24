from flask import Flask, render_template, request, jsonify
from lexer import Lexer
from parserr import Parser


app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
	if request.method == 'POST': 
		code = request.form['code'].replace('\r','').split('\n')

		lexer = Lexer(code)
		parser = Parser()

		parser.parser(lexer.lexer())

		if parser.get_web_output():
			return render_template('index.html',web_output='\n'.join(str(el) for el in parser.get_web_output()))
	return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
	if request.args.get('code'):
		lexer = Lexer(request.args.get('code').replace('\r','').split('\n'))
		parser = Parser()
		parser.parser(lexer.lexer())

		return jsonify([{'code' : parser.get_web_output()}])
	return render_template('api.html')

if __name__ == "__main__":
	app.run(debug=True)
