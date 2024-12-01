import os
from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/env')
def test_env():
    return f'{os.environ['MYSQL_USER']} - {os.environ['MYSQL_PASSWORD']}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
