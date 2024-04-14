from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField # type: ignore
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange # type: ignore
from flask import flash
from flask_sqlalchemy import User
from wtforms.fields import DateField # type: ignore
from flask_wtf.file import FileField, FileAllowed
from werkzeug.security import check_password_hash

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    sex = SelectField('Sex', choices=[('Man', 'Man'), ('Woman', 'Woman')])
    submit = SubmitField("Sign Up")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('This email address is already registered.')
            raise ValidationError('This email address is already registered.')
        if not any(char in ['@'] for char in email.data):
            flash('Incorrect e-mail address.')
            raise ValidationError('Incorrect e-mail address.')
        if not any(char in ['.'] for char in email.data):
            flash('Incorrect e-mail address.')
            raise ValidationError('Incorrect e-mail address.')
        if len(email.data) < 5:
            flash('Incorrect e-mail address.')
            raise ValidationError('Incorrect e-mail address.')
        if len(email.data) > 30:
            flash('Incorrect e-mail address.')
            raise ValidationError('Incorrect e-mail address.')
        if 'admin' in email.data:
            flash('You cannot use the word "admin" in your email address.')
            raise ValidationError('You cannot use the word "admin" in your email address.')
            
    def validate_password(self, password):
        if len(password.data) < 8:
            flash('The password must be at least 8 characters long.')
            raise ValidationError('The password must be at least 8 characters long.')
        if not any(char.isdigit() for char in password.data):
            flash('The password must contain at least one digit.')
            raise ValidationError('The password must contain at least one digit.')
        if not any(char.isupper() for char in password.data):
            flash('The password must contain at least one uppercase letter.')
            raise ValidationError('The password must contain at least one uppercase letter.')
        if not any(char.islower() for char in password.data):
            flash('The password must contain at least one lowercase letter.')
            raise ValidationError('The password must contain at least one lowercase letter.')
        if not any(char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '='] for char in password.data):
            flash('The password must contain at least one special character.')
            raise ValidationError('The password must contain at least one special character.')

    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != self.password.data:
            flash('Passwords must be the same.')
            raise ValidationError('Passwords must be the same.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Log In")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            flash('Login is incorrect.')
            raise ValidationError('Login is incorrect.')

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description')
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    product_image = StringField('Product Image', validators=[DataRequired()])
    submit = SubmitField('Add Product')

class OrderForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    total_price = FloatField('Total Price', validators=[DataRequired(), NumberRange(min=0)])
    order_date = DateTimeField('Order Date', validators=[DataRequired()])
    submit = SubmitField('Place Order')    

class EditProductForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    isbn = StringField('ISBN', validators=[Length(min=10, max=13)])
    description = TextAreaField('Description')
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    current_quantity = IntegerField('Current Quantity', validators=[DataRequired(), NumberRange(min=0)])
    total_quantity = IntegerField('Total Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Update Product')

    def validate_total_quantity(self, total_quantity):
        if total_quantity.data < 0:
            raise ValidationError('Total quantity cannot be negative.')

    def validate_current_quantity(self, current_quantity):
        if current_quantity.data < 0:
            raise ValidationError('Current quantity cannot be negative.')

class DeleteproductForm(FlaskForm):
    product = StringField('Product name', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Remove product")

class DeleteUser(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Delete user")

