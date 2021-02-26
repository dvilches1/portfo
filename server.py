from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv
app = Flask(__name__)

#Homepage
@app.route('/')
def hello_world():
	return render_template('index.html')
#other pages
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

#Contact form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Algo salió mal.'
	else:
		return 'something went wrong. Try again!'

def write_to_file(data):
	with open('database.txt', 'a') as database:
			registro = ''
			for value in data.values():
				registro += value + ';'
			database.write(f'\n{registro}{datetime.now()}')
			#database.write('{}\n'.format(registro + str(datetime.now())))
			database.close()

def write_to_csv(data):
	with open('database.csv', 'a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		date = datetime.now()
		csv_writer = csv.writer(database2, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message, date])