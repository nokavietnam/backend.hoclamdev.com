from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('FLASK_CONFIG')
    
    @app.route("/")
    def home():
        return "Hello, Flask with WSGI!"

    return app

