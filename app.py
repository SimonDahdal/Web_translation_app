"""
Flask application serving as a simple translation service. 
It receives text and a target language, uses an external API for translation, 
and stores the results in a database.
"""

from flask import Flask, request, jsonify, render_template
from models import db, Translation
from translation_client import translate_text

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
    original_text = data.get('text')
    target_language = data.get('target_language')
    if not original_text or not target_language:
        return jsonify({'error': 'Missing text or target language'}), 400

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