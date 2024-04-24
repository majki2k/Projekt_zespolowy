
from app.forms import RegistrationForm, LoginForm, ProductForm
from app import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    Form = RegistrationForm()
    if Form.validate_on_submit():
        if request.method == 'POST':
            user = User(username=Form.username.data, email=Form.email.data, password=Form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Accont has been created!")
            return redirect(url_for('login'))
    
    return render_template('register.html', form = Form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    Form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        return redirect(url_for('index'))

    return render_template('login.html', form = Form)


@app.route('/product', methods=['GET'])
def product():
    Form = ProductForm()
    if request.method =='GET':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('Price')
        quantity = request.form.get('Quantity')
        product_image = request.form.get('Product Image')
        return redirect(url_for('product'))
    return render_template('shop.html', form = Form)
