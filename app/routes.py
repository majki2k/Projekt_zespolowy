
from curses import flash
from app.forms import RegistrationForm, LoginForm, ProductForm
from app import app
from app import db
from app import os
from flask import Flask, render_template, request, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    Form = RegistrationForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

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
        image_file = 'default_item.img'
        image_path = os.path.join(app.root_path, 'static/img', image_file)
        form.image.data.save(image_path)
 
        
        existing_item = item.query.filter_by(name=form.name.data).first()
       
        if existing_item:
            existing_item.total_quantity += form.total_quantity.data
            existing_item.current_quantity += form.total_quantity.data
            flash('Ilość przedmiotów zaktualizowana!')
        else:
            item = item(name=form.title.data, description=form.description.data, price=form.price.data,
                        quantity=form.quantity.data, product_image=image_file,
                        current_quantity=form.total_quantity.data, total_quantity=form.total_quantity.data)
            db.session.add(item)
            flash('Przedmiot dodany!')
 
        db.session.commit()
        return redirect(url_for('routes.additem'))
 
    if form.errors:
        flash('Validation Errors: ' + str(form.errors))
    return render_template('add_item.html', title='Add Item', form=form)