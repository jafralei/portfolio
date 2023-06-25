from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

print(__name__)

#To activate debug type "export FLASK_DEBUG=1"

# pri   nt(url_for('static', filename='poke.ico'))

@app.route('/') #home
def my_home():
    # print(url_for('static', filename='poke.ico'))
    return render_template('index.html')     #looks files into templates folder

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
    with open('database.txt',mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode = 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #give us a dict
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not saved to database'
    else:
        return 'something went wrong'


# @app.route('/about.html')
# def about():
#     return render_template('about.html') 

# @app.route('/components.html')
# def components():
#     return render_template('components.html') 

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html') 

# @app.route('/thankyou.html')
# def thank():
#     return render_template('thankyou.html') 

# @app.route('/work.html')
# def work():
#     return render_template('work.html') 

# @app.route('/works.html')
# def works():
#     return render_template('works.html') 


