import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
from validators import validate_translation_request

def test_validate_translation_request():
    # Test valid input
    data = {'text': 'Hello', 'target_language': 'French'}
    assert validate_translation_request(data) == (True, None)

    # Test missing text
    data = {'text': '', 'target_language': 'French'}
    assert validate_translation_request(data) == (False, 'Missing text or target language')

    # Test missing target_language
    data = {'text': 'Hello', 'target_language': ''}
    assert validate_translation_request(data) == (False, 'Missing text or target language')

    # Test invalid text input
    data = {'text': 123, 'target_language': 'French'}
    assert validate_translation_request(data) == (False, 'Invalid text input')

    # Test invalid target_language
    data = {'text': 'Hello', 'target_language': 'Spanish'}
    assert validate_translation_request(data) == (False, 'Invalid target language')
