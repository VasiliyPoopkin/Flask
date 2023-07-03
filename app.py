from flask import Flask
from flask import jsonify
import logging


app = Flask(__name__)

@app.route('/hello')
def hello():
    app.logger.info('Accessed /hello endpoint.')
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

@app.route('/hello/html')
def hello_html():
    app.logger.info('Accessed /hello/html endpoint.')
    return '<h1>Hello, world!</h1>'

@app.route('/hello/json')
def hello_json():
    app.logger.info('Accessed /hello/json endpoint.')
    return jsonify(message='Hello, world!')

logging.basicConfig(level=logging.INFO)

@app.route('/hello')
def hello():
    app.logger.info('Accessed /hello endpoint.')
    return 'Hello, world!'

@app.route('/hello/html')
def hello_html():
    app.logger.info('Accessed /hello/html endpoint.')
    return '<h1>Hello, world!</h1>'

@app.route('/hello/json')
def hello_json():
    app.logger.info('Accessed /hello/json endpoint.')
    return jsonify(message='Hello, world!')