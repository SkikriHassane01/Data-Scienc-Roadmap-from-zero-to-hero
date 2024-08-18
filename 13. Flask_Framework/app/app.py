## we will create a flask example to show how to use flask framework
## we will create a simple web page with a form to take input from user and display the input on the web page
## also we will use some jinja templating to display the input on the web page
## {{ name }} is a jinja templating syntax to display the value of name variable
## {% %} is a jinja templating syntax to write python code in html file

from flask import Flask, render_template, request

# create a flask app
app = Flask(__name__)

# define a route for the default page
@app.route('/')
def index():
    return render_template('index.html')

# define a route for the form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    return render_template('submit.html', name=name, age= age)

# define a route for the about page 
# run the app
if __name__ == '__main__':
    app.run(debug=True)

