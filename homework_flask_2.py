dimport random
from flask import request, redirect, abort


#task 1


@app.route('/users')
def get_users():
    names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Olivia']
    random_names = random.sample(names, random.randint(1, len(names)))
    app.logger.info('Accessed /users endpoint.')
    return ', '.join(random_names)git remote add origin https://github.com/VasiliyPoopkin/Flask.git

@app.route('/books')
def get_books():
    books = ['The Great Gatsby', 'To Kill a Mockingbird', 'Pride and Prejudice', '1984', 'The Catcher in the Rye']
    random_books = random.sample(books, random.randint(1, len(books)))
    app.logger.info('Accessed /books endpoint.')

    html_list = '<ul>'
    for book in random_books:
        html_list += f'<li>{book}</li>'
    html_list += '</ul>'

    return html_list


#task 2


@app.route('/users/<int:id>')
def get_user(id):
    if id % 2 == 0:
        app.logger.info(f'Accessed /users/{id} endpoint.')
        return f'Text with id: {id}'
    else:
        app.logger.info(f'404 Not Found: /users/{id} endpoint.')
        return 'Not Found', 404

@app.route('/books/<string:title>')
def get_book(title):
    transformed_title = title.capitalize()
    app.logger.info(f'Accessed /books/{title} endpoint.')
    return transformed_title


#task 3


@app.route('/params')
def get_params():
    params = request.args
    app.logger.info(f'Accessed /params endpoint with query parameters: {params}')

    table_html = '<table>'
    table_html += '<tr><th>parameter</th><th>value</th></tr>'
    for key, value in params.items():
        table_html += f'<tr><td>{key}</td><td>{value}</td></tr>'
    table_html += '</table>'

    return table_html


#task 4


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        app.logger.info('Accessed /login endpoint with GET request.')
        return '''
            <form method="POST" action="/login">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br>
                <input type="submit" value="Submit">
            </form>
        '''
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        app.logger.info(f'Accessed /login endpoint with POST request. Username: {username}, Password: {password}')

        if username and password:
            return redirect('/users')
        else:
            abort(400, 'Missing username or password')


#task 5


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('404 Not Found')
    return '''
        <h1>404 Not Found</h1>
        <p>The requested page could not be found.</p>
    ''', 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('500 Internal Server Error')
    return '''
        <h1>500 Internal Server Error</h1>
        <p>An internal server error occurred.</p>
    ''', 500


#task 6


@app.route('/')
def index():
    app.logger.info('Accessed / endpoint.')
    return '''
        <h1>Welcome to the Homepage</h1>
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/users">Users</a></li>
            <li><a href="/books">Books</a></li>
            <li><a href="/params">Params</a></li>
        </ul>
    '''


#task 7


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
    return ', '.join(random_names)

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

    app.logger.info('Accessed /books endpoint.')

    html_list = '<ul>'
    for book in random_books:
        html_list += f'<li>{book}</li>'
    html_list += '</ul>'

    return html_list


#task 8


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if len(username) < 5:
        return 'Invalid username. Username must be at least 5 characters long.', 400

    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
        return 'Invalid password. Password must be at least 8 characters long and contain at least 1 digit and 1 uppercase letter.', 400

    app.logger.info(f'Accessed /login endpoint with POST request. Username: {username}, Password: {password}')

    return redirect('/users')