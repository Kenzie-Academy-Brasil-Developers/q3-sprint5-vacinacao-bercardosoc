from flask import Flask
from flask_migrate import Migrate

mg = Migrate()

def init_app(app: Flask):
    
    mg.init_app(app=app, db=app.db)
    
    # Migrate(app=app, db=app.db, compare_type=True)