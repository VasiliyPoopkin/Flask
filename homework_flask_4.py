from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template


#task 1

load_dotenv('.env')

secret_key = os.getenv('SECRET_KEY')
database_name = os.getenv('DATABASE_NAME')
host = os.getenv('HOST')
port = os.getenv('PORT')
other_value = os.getenv('OTHER_VALUE')

#task 3

load_dotenv('.env')

app = Flask(__name__)

secret_key = os.getenv('SECRET_KEY')
database_name = os.getenv('DATABASE_NAME')
host = os.getenv('HOST')
port = os.getenv('PORT')
other_value = os.getenv('OTHER_VALUE')

app.config['SECRET_KEY'] = secret_key
app.config['DATABASE_NAME'] = database_name
app.config['HOST'] = host
app.config['PORT'] = port
app.config['OTHER_VALUE'] = other_value

@app.route('/')
def index():
    secret_key = app.config['SECRET_KEY']
    return 'Hello, World!'


#task 4

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:sqlite:identifier.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)

if __name__ == '__main__':
    db.create_all()

    app.run()

users = User.query.all()
for user in users:
    print(user.name, user.email)

new_book = Book(title='Назва книги', author='Автор книги', price=19.99)
db.session.add(new_book)
db.session.commit()


#task 5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:sqlite:identifier.sqlite'
db = SQLAlchemy(app)


@app.route('/users')
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify(users_list)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    else:
        return 'User not found', 404

@app.route('/books')
def get_books():
    books = Book.query.all()
    books_list = []
    for book in books:
        books_list.append({'id': book.id, 'title': book.title, 'author': book.author, 'price': book.price})
    return jsonify(books_list)

@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'price': book.price})
    else:
        return 'Book not found', 404

@app.route('/purchases')
def get_purchases():
    purchases = Purchase.query.all()
    purchases_list = []
    for purchase in purchases:
        purchases_list.append({'id': purchase.id, 'user_id': purchase.user_id, 'book_id': purchase.book_id, 'purchase_date': purchase.purchase_date})
    return jsonify(purchases_list)

@app.route('/purchases/<int:purchase_id>')
def get_purchase(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    if purchase:
        return jsonify({'id': purchase.id, 'user_id': purchase.user_id, 'book_id': purchase.book_id, 'purchase_date': purchase.purchase_date})
    else:
        return 'Purchase not found', 404

if __name__ == '__main__':
    app.run()


#task 6


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:sqlite:identifier.sqlite'
db = SQLAlchemy(app)


@app.route('/purchases')
def get_purchases():
    purchases = db.session.query(Purchase, User, Book).join(User).join(Book).all()
    purchases_list = []
    for purchase, user, book in purchases:
        purchases_list.append({
            'purchase_id': purchase.id,
            'user_id': user.id,
            'user_name': user.name,
            'book_id': book.id,
            'book_title': book.title,
            'purchase_date': purchase.purchase_date
        })
    return jsonify(purchases_list)

@app.route('/purchases/<int:purchase_id>')
def get_purchase(purchase_id):
    purchase = db.session.query(Purchase, User, Book).join(User).join(Book).filter(Purchase.id == purchase_id).first()
    if purchase:
        purchase_info = {
            'purchase_id': purchase.Purchase.id,
            'user_id': purchase.User.id,
            'user_name': purchase.User.name,
            'book_id': purchase.Book.id,
            'book_title': purchase.Book.title,
            'purchase_date': purchase.Purchase.purchase_date
        }
        return jsonify(purchase_info)
    else:
        return 'Purchase not found', 404

if __name__ == '__main__':
    app.run()


#task 7

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:sqlite:identifier.sqlite'
db = SQLAlchemy(app)


@app.route('/users', methods=['POST'])
def create_user():
    if request.content_type == 'application/json':
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    elif request.content_type == 'application/x-www-form-urlencoded':
        name = request.form.get('name')
        email = request.form.get('email')
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    else:
        return jsonify({'error': 'Invalid content type'}), 400

@app.route('/books', methods=['POST'])
def create_book():
    if request.content_type == 'application/json':
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'], price=data['price'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book created successfully'})
    elif request.content_type == 'application/x-www-form-urlencoded':
        title = request.form.get('title')
        author = request.form.get('author')
        price = request.form.get('price')
        new_book = Book(title=title, author=author, price=price)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book created successfully'})
    else:
        return jsonify({'error': 'Invalid content type'}), 400

@app.route('/purchases', methods=['POST'])
def create_purchase():
    if request.content_type == 'application/json':
        data = request.get_json()
        user_id = data['user_id']
        book_id = data['book_id']
        user = User.query.get(user_id)
        book = Book.query.get(book_id)
        if user and book:
            new_purchase = Purchase(user_id=user_id, book_id=book_id)
            db.session.add(new_purchase)
            db.session.commit()
            return jsonify({'message': 'Purchase created successfully'})
        else:
            return jsonify({'error': 'User or Book not found'}), 404
    elif request.content_type == 'application/x-www-form-urlencoded':
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')
        user = User.query.get(user_id)
        book = Book.query.get(book_id)
        if user and book:
            new_purchase = Purchase(user_id=user_id, book_id=book_id)
            db.session.add(new_purchase)
            db.session.commit()
            return jsonify({'message': 'Purchase created successfully'})
        else:
            return jsonify({'error': 'User or Book not found'}), 404
    else:
        return jsonify({'error': 'Invalid content type'}), 400

if __name__ == '__main__':
    app.run()