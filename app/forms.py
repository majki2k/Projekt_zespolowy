from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask import flash
from flask_sqlalchemy import User, Book
from wtforms.fields import DateField
from flask_wtf.file import FileField, FileAllowed
from werkzeug.security import check_password_hash

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    sex = SelectField('Płeć', choices=[('Mężczyzna', 'Mężczyzna'), ('Kobieta', 'Kobieta')])
    submit = SubmitField("Sign Up")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('Ten adres e-mail jest już zarejestrowany.')
            raise ValidationError('Ten adres e-mail jest już zarejestrowany.')
        if not any(char in ['@'] for char in email.data):
            flash('Nieprawidłowy adres e-mail.')
            raise ValidationError('Nieprawidłowy adres e-mail.')
        if not any(char in ['.'] for char in email.data):
            flash('Nieprawidłowy adres e-mail.')
            raise ValidationError('Nieprawidłowy adres e-mail.')
        if len(email.data) < 5:
            flash('Nieprawidłowy adres e-mail.')
            raise ValidationError('Nieprawidłowy adres e-mail.')
        if len(email.data) > 30:
            flash('Nieprawidłowy adres e-mail.')
            raise ValidationError('Nieprawidłowy adres e-mail.')
        if 'admin' in email.data:
            flash('Nie można używać słowa "admin" w adresie e-mail.')
            raise ValidationError('Nie można używać słowa "admin" w adresie e-mail.')
            
    def validate_password(self, password):
        if len(password.data) < 8:
            flash('Hasło musi mieć co najmniej 8 znaków.')
            raise ValidationError('Hasło musi mieć co najmniej 8 znaków.')
        if not any(char.isdigit() for char in password.data):
            flash('Hasło musi zawierać co najmniej jedną cyfrę.')
            raise ValidationError('Hasło musi zawierać co najmniej jedną cyfrę.')
        if not any(char.isupper() for char in password.data):
            flash('Hasło musi zawierać co najmniej jedną wielką literę.')
            raise ValidationError('Hasło musi zawierać co najmniej jedną wielką literę.')
        if not any(char.islower() for char in password.data):
            flash('Hasło musi zawierać co najmniej jedną małą literę.')
            raise ValidationError('Hasło musi zawierać co najmniej jedną małą literę.')
        if not any(char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '='] for char in password.data):
            flash('Hasło musi zawierać co najmniej jeden znak specjalny.')
            raise ValidationError('Hasło musi zawierać co najmniej jeden znak specjalny.')

    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != self.password.data:
            flash('Hasła muszą być takie same.')
            raise ValidationError('Hasła muszą być takie same.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Log In")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            flash('Login jest nieprawidłowy.')
            raise ValidationError('Login jest nieprawidłowy.')
    


class BookForm(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    product = StringField('ID', validators=[DataRequired()])
    order = StringField('ID', validators=[DataRequired()])

class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=2, max=100)])
    isbn = StringField('ISBN', validators=[Length(min=10, max=13)])
    description = TextAreaField('Description')
    image = FileField('Book Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    current_quantity = IntegerField('Current Quantity', validators=[DataRequired(), NumberRange(min=0)])
    total_quantity = IntegerField('Total Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Update Book')

    def validate_total_quantity(self, total_quantity):
        if total_quantity.data < 0:
            raise ValidationError('Total quantity cannot be negative.')

    def validate_current_quantity(self, current_quantity):
        if current_quantity.data < 0:
            raise ValidationError('Current quantity cannot be negative.')

class DeleteproductForm(FlaskForm):
    product = StringField('Product name', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Usuń produkt")

class DeleteUser(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Usuń użytkownika")

class RateBookForm(FlaskForm):
    rating = SelectField('Rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int)
    submit = SubmitField('Rate')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class ReviewForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=2000)])
    submit = SubmitField('Add Review')

class DeleteReviewForm(FlaskForm):
    review = StringField('Review', validators=[DataRequired()])
    confirm = BooleanField('Confirm Delete')
    submit = SubmitField("Usuń opinię")

class EditCommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update Comment')