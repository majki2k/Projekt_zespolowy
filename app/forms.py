from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange 
from flask import flash
from flask_wtf.file import FileField, FileAllowed


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Log In")

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


class DeleteproductForm(FlaskForm):
    product = StringField('Product name', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Remove product")

class DeleteUser(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Delete user")


