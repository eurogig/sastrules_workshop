from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import html

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = html.escape(request.form['name'])
        email = html.escape(request.form['email'])

        # Log the data to a file
        log_data(name, email)

        return render_template('reply.html', name=name, email=email)

    return render_template('index.html')

def log_data(name, email):
    with open('data.log', 'a') as log_file:
        log_file.write(f'Name: {name}, Email: {email}\n')

if __name__ == '__main__':
    app.run(debug=True)
