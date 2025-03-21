# Web Translate App

A web application that translates text into a selected language using the Ollama API. The application is divided into modular components: a frontend interface for user input, a Flask-based backend for processing translation requests, and an SQLite database for storing translation history.

## Features
- **User-friendly Interface:**
  - Input area for text.
  - Dropdown to select target language.
  - Display area for the translated text.
- **Backend API:**
  - REST endpoint `/translate` to handle translation requests.
  - Integration with the Ollama API for text translation.
- **Database:**
  - SQLite database for saving translation records.
  - SQLAlchemy for ORM-based database interactions.

## Technologies Used
- **Python**: Main programming language.
- **Flask**: Web framework for API development.
- **SQLite**: Lightweight database for storing translations.
- **SQLAlchemy**: ORM for database operations.
- **HTML/CSS/JavaScript**: Frontend technologies.
- **Requests**: Python library to interact with external APIs.

## Project Structure
```
Web_translate_app/
├── app.py                       # Main Flask application
├── translation_client.py        # Handles communication with the Ollama API
├── models.py                    # Database models using SQLAlchemy
├── validators.py                # Input validation functions
├── requirments.txt              # Project dependencies
├── templates/
│   └── index.html               # Frontend HTML
├── static/
│   ├── main.js                  # JavaScript for frontend logic
│   └── styles.css               # CSS for styling the application
├── test/                       # Unit tests for the application
│   ├── ollama.py
│   ├── translation_test.py
│   └── validators_test.py
└── instance/
    └── translations.db         # SQLite database for storing translation records
```
## Ollama installation and setup

1. Run the following script:

    ``` bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
2. Disable Ollama service

    ``` bash
    sudo systemctl disable --now ollama.service
    ```

3. Start ollama:

    ``` bash
    ollama serve
    ```

4. Pull the model:

    ``` bash
    ollama pull gemma3:1b
    ```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SimonDahdal/Web_translation_app.git
   cd Web_translate_app
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source venv/bin/activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Start the Ollama API server:
   ```bash
   ollama serve
   ```
2. Start the Flask development server:
   ```bash
   python app.py
   ```
3. Access the application:
   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000)

## How It Works
- **Frontend:**
  The user enters text and selects a target language. On submitting the form, JavaScript sends an AJAX request to the `/translate` endpoint.
- **Backend:**
  The Flask app receives the request, calls the `translate_text` function from `translation_client.py` to interact with the Ollama API, and stores the original and translated texts in the SQLite database before returning the translation in JSON format.
- **Database:**
  The translations are saved using the SQLAlchemy ORM, which simplifies interactions with the SQLite database.

## License
MIT License.

## Acknowledgements
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Ollama API](https://ollama.com/)

