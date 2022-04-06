from flask import Flask
from app.routes.vacines_route import bp_vacine

def init_app(app: Flask):
    app.register_blueprint(bp_vacine)
