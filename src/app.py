import psycopg2
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
from mailAuth import mailAuth

# Models:
from models.ModelUser import ModelUser
from models.ModelCode import ModelCode
from models.entities.Code import Code

# Entities:
from models.entities.User import User

app = Flask(__name__)

# DB Connection:
try:
    connection = psycopg2.connect(
        host = 'host',
        user = 'user',
        password = 'password',
        database = 'database'

    )
except Exception as ex:
    raise Exception(ex)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(connection, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['user'], request.form['password'])
        logged_user = ModelUser.login(connection, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('profile'))
            else:
                flash('Contraseña Incorrecta')
                return render_template('auth/login.html')
        else:
            flash('Usuario Incorrecto')
            return render_template('auth/login.html')
            
    # Redirección a Perfil con OAUTH
    if request.method == 'GET':
        user = User(0, 'username', 'password')
        logged_user = ModelUser.login(connection, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('profile'))
    else:
        return render_template('auth/login.html')
    

@app.route('/logout')
def logout():
    logout_user()
    return render_template('auth/login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/code')
def code():
    check_table = ModelCode.clearTable(connection)
    added_number = ModelCode.addCode(connection)
    code_number = ModelCode.getCode(connection)
    email = mailAuth.sendEmail(code_number)
    print('Email Status:', email)
    if email:
        return render_template('auth/validation_code.html')
    else:
        return render_template('auth/login.html')

@app.route('/validation_code',  methods=['GET', 'POST'])
def validation_code():
    if request.method == 'POST':
        code = Code(request.form['code'])
        checked_code = ModelCode.checkCode(connection, code)
        if checked_code != None:
            user = User(0, 'username', 'password')
            logged_user = ModelUser.login(connection, user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    return redirect(url_for('profile'))
        else:
            flash('Invalid password')
            return render_template('auth/validation_code.html')
    else:
        return render_template('auth/validation_code.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()