from flask import Flask

app = Flask(__name__)

@app.route('/')

def get_index():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5010,
        debug = True
    )