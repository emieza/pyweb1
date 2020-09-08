from flask import Flask
app = Flask(__name__)


# global vars
equips = [ "Cornellà", "Sant Boi", "Despí" ]


# entry points

@app.route('/')
def hello_world():
	html = ""
	for equip in equips:
		html += equip + "<br>"
	return 'Hello, World!<br><br>' + html + "<a href='/afegir_equip'>Afegir equip</a>"


@app.route('/afegir_equip')
def afegir_equip():
	return """
<form method='post'>
	Introdueix nou equip:
	<input name='equip' type='text' />
	<br>
	<input type='submit'>
</form>
"""


from flask import request

@app.route('/afegir_equip', methods=['POST'])
def afegir_equip_post():
	equip = request.form["equip"]
	equips.append(equip)
	return "Afegit: " + equip + "<br><br><a href='/'>Anar a inici</a>"



app.run()


