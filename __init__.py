from flask import Flask
from .views import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)