"""
Flask application serving as a simple translation service. 
It receives text and a target language, uses an external API for translation, 
and stores the results in a database.

# Prompt Comment to generate this file:
Create a Flask application that serves as a simple translation service.
The application should:
1. Render a main index page accessible via GET at '/'.
2. Provide a '/translate' endpoint accessible via POST that:
   a. Receives JSON data containing 'text' and 'target_language'.
   b. Validates the input using a function 'validate_translation_request' from validators.py.
   c. If validation fails, returns a JSON error response with HTTP status 400.
   d. Translates the given text by calling 'translate_text' from translation_client.py.
   e. Saves the translation record into a database using SQLAlchemy (model: Translation).
   f. Returns the translated text as a JSON response.
3. Configure SQLAlchemy with a SQLite database named 'translations.db'.
4. Ensure that the database and all tables are created on application startup.

"""

from flask import Flask, request, jsonify, render_template
from models import db, Translation

from translation_client import translate_text
from validators import validate_translation_request  # Import the validator

# Create the Flask application.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///translations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create all tables once within the application context.
with app.app_context():
    db.create_all() 


@app.route('/', methods=['GET'])
def index():
    """
    Renders the main web page.
    """
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    """
    Receives JSON containing 'text' and 'target_language'.
    Translates the text, saves the result in the database,
    and returns the translated text as JSON.
    """
    data = request.get_json()
    
    is_valid, error_message = validate_translation_request(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    original_text = data.get('text')
    target_language = data.get('target_language')

    translated_text = translate_text(original_text, target_language)

    # Save translation to the database.
    new_translation = Translation(
        original_text=original_text,
        translated_text=translated_text,
        target_language=target_language
    )
    db.session.add(new_translation)
    db.session.commit()

    return jsonify({'translated_text': translated_text})


if __name__ == '__main__':
    app.run(debug=True)

