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
