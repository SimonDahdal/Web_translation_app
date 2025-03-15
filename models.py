from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.Text, nullable=False)
    translated_text = db.Column(db.Text, nullable=False)
    target_language = db.Column(db.String(50), nullable=False)