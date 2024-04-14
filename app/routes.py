from flask import render_template
from app import app
from flask import Flask, render_template, request, redirect, url_for
from flask_login import UserMixin, login_user

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Create a new user
        new_user = User(email=email, password=password)

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('profile'))
        else:
            error_message = "Invalid login credentials. Please try again."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)