from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Log the data to a file
        log_data(name, email)

        reply = f'Thank you, {name}! Your email ({email}) has been logged.'

        return reply

    return render_template('index.htm')

def log_data(name, email):
    with open('data.log', 'a') as log_file:
        log_file.write(f'Name: {name}, Email: {email}\n')

if __name__ == '__main__':
    app.run(debug=True)
