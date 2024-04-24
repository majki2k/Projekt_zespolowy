
from curses import flash
from app.forms import RegistrationForm, LoginForm, ProductForm
from app.models import Product, User, Order
from app import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from app.models import User
import os
from werkzeug.utils import secure_filename


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


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ProductForm()
    if form.validate_on_submit():
        product_image = 'default_image.png'

        if form.product_image.data:
            product_image_file = secure_filename(form.product_image.data.filename)
            product_image_path = os.path.join(app.root_path, 'static/img', product_image_file)
            form.product_image.data.save(product_image_path)
 
        
        existing_item = Product.query.filter_by(name=form.name.data).first()
       
        if existing_item:
            existing_item.quantity += form.quantity.data
            flash('Ilość przedmiotów zaktualizowana!')
        else:
            item = Product(name=form.name.data, description=form.description.data, price=form.price.data,
                        quantity=form.quantity.data, product_image=product_image)
            db.session.add(item)
            flash('Przedmiot dodany!')
 
        db.session.commit()
        return redirect(url_for('add_item'))
 
    if form.errors:
        flash('Validation Errors: ' + str(form.errors))
    return render_template('add_item.html', title='Add Item', form=form)