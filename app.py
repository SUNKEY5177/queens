from flask import Flask, request
from flask_cors import CORS

from utils import trigger

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/queens_list')
def queens_list():
    size = request.args.get("size")
    res = trigger(int(size))
    return res


if __name__ == '__main__':
    app.run()
