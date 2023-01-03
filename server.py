from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


def escrever_os_dados(data):
    with open('webserver/database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}') 


def escrever_arquivo_csv(data):
    with open('webserver/database2.csv', mode='a', newline="") as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            escrever_arquivo_csv(data)
            return redirect('/thankyou.html')
    except:
        return 'não foi salvo na base de dados'
    else:
        return'something went wrong. Try again!!'


