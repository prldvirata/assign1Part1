from django.apps import AppConfig
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['https://assign1part2.netlify.app/skill-list'])


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
