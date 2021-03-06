from flask import Flask, render_template, request, flash
from model import *

app = Flask(__name__, template_folder="templates")
model = Model()

@app.route("/", methods=['GET', 'POST'])
def index():
	json = {
	"title"	: 'MTW-Barris',
	"logo" : '../static/images/logo.jpg'
	}
	if request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		number = request.form['number']
		message = request.form['message']

		if model.send(name, email, number, message):
			flash("data successfully add")
		else:
			flash("data not successfully add")
		return render_template("index.html", data=json)
	else:
		return render_template("index.html", data=json)

@app.route('/jadwal', methods=['GET'])
def jadwal():
	json = {
	"title": 'MTW-Barris',
	"logo": '../static/images/logo.jpg',
	"jadwal": model.read()
	}
	return render_template('jadwal.html', data=json)
