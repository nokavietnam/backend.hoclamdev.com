import os
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

app.config.from_pyfile('settings.py')

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
# app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
# app.config['MYSQL_DB'] = 'database_name'

db_config = {
    'host': 'localhost',
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'database': 'mqembhdihosting_backend'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/env')
def test_env():
    return f'{os.environ['MYSQL_USER']} - {os.environ['MYSQL_PASSWORD']}'

@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM be_post")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
