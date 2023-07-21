from flask import render_template
from flask import session, redirect, url_for
from functools import wraps
from urllib import request
from random import random
from Flask import app


#task 1

@app.route('/users')
def get_users():
    names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Olivia']

    count = request.args.get('count')
    if count:
        try:
            count = int(count)
            if count <= 0:
                return 'Invalid count parameter. Count must be a positive integer.', 400
            random_names = random.sample(names, count)
        except ValueError:
            return 'Invalid count parameter. Count must be a positive integer.', 400
    else:
        random_names = random.sample(names, random.randint(1, len(names)))

    app.logger.info('Accessed /users endpoint.')
    return render_template('@app.route('/users')')

@app.route('/books')
def get_books():
    books = ['The Great Gatsby', 'To Kill a Mockingbird', 'Pride and Prejudice', '1984', 'The Catcher in the Rye']

    count = request.args.get('count')
    if count:
        try:
            count = int(count)
            if count <= 0:
                return 'Invalid count parameter. Count must be a positive integer.', 400
            random_books = random.sample(books, count)
        except ValueError:
            return 'Invalid count parameter. Count must be a positive integer.', 400
    else:
        random_books = random.sample(books, random.randint(1, len(books)))

    app.logger.info('Accessed /users endpoint.')
    return render_template

#task 2

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if len(username) < 5:
        return 'Invalid username. Username must be at least 5 characters long.', 400

    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
        return 'Invalid password. Password must be at least 8 characters long and contain at least 1 digit and 1 uppercase letter.', 400

    app.logger.info(f'Accessed /login endpoint with POST request. Username: {username}, Password: {password}')

    session['username'] = username

    return redirect('/users')

app.secret_key = 'your_secret_key'

#task 3

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    app.logger.info('Accessed / endpoint.')
    username = session['username']
    return f'<h1>Hello, {username}</h1><p>Welcome to the Homepage</p>'

@app.route('/users')
@login_required
def get_users():

@app.route('/params')
@login_required
def get_params():

#task 4

@app.route('/')
@login_required
def index():
    app.logger.info('Accessed / endpoint.')
    return render_template('index.html', logged_in=True, username=session['username'])

@app.route('/users')
@login_required
def get_users():
    return render_template('users.html', logged_in=True, username=session['username'])
