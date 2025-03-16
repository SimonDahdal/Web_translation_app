# Prompt Comment to generate this file:
# Create a Python module that sets up SQLAlchemy for a Flask application.
# The module should:
# 1. Import SQLAlchemy from flask_sqlalchemy.
# 2. Create a SQLAlchemy object named 'db'.
# 3. Define a 'Translation' model with the following columns:
#    - id: An Integer primary key.
#    - original_text: A non-nullable Text field.
#    - translated_text: A non-nullable Text field.
#    - target_language: A non-nullable String field with a maximum length of 50.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.Text, nullable=False)
    translated_text = db.Column(db.Text, nullable=False)
    target_language = db.Column(db.String(50), nullable=False)