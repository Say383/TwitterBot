
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for

# Flask app setup (for demonstration)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class User(UserMixin):
    # User class with password hashing (assuming a user model with a password_hash field)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Example login route using Flask-Login and Flask-WTF
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import os
from cryptography.fernet import Fernet

class User(UserMixin):
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class SecurityManager:
    def __init__(self):
        self.login_manager = LoginManager()
        self.key = os.environ.get('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        return self.cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode()

    def log_error(self, error_message):
        logging.error(error_message)

# Example usage
security_manager = SecurityManager()
encrypted_data = security_manager.encrypt_data("Sensitive Information")
decrypted_data = security_manager.decrypt_data(encrypted_data)
