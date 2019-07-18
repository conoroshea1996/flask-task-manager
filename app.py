from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def method_name():
    return '<h1> hello world </h1>'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
