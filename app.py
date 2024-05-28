#!/usr/bin/python3

from flask import Flask
from config import Config
from routes.auth_routes import auth_bp
from routes.tutorial_routes import tutorial_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(tutorial_bp, url_prefix='/tutorials')

if __name__ == '__main__':
    app.run(debug=True)
