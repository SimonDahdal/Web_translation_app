# Prompt Comment to generate this file:
# Create a Python module that validates translation request data.
# The module must define a function 'validate_translation_request' that:
# 1. Receives a dictionary with keys 'text' and 'target_language'.
# 2. Checks whether both keys exist. If not, returns (False, 'Missing text or target language').
# 3. Validates that the 'text' value is a non-empty, properly formatted string. If invalid, returns (False, 'Invalid text input').
# 4. Ensures that 'target_language' is one of the allowed languages: English, French, or German.
# 5. Returns (True, None) if the data is valid.

def validate_translation_request(data):
    """
    Validates the translation request data.
    Returns (True, None) if valid, otherwise returns (False, error_message).
    """
    original_text = data.get('text')
    target_language = data.get('target_language')
    
    if not original_text or not target_language:
        return False, 'Missing text or target language'
    
    if not isinstance(original_text, str) or not original_text.strip():
        return False, 'Invalid text input'
    
    allowed_languages = ['English', 'French', 'German']

    if target_language not in allowed_languages:
        return False, 'Invalid target language'
    
    return True, None
