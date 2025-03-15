# UnitTest translate_text function
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from translation_client import translate_text

def test_translate_text():
    text = "Hello"
    target_language = "French"
    translation = translate_text(text, target_language)
    assert isinstance(translation, str)
    assert translation != f"Error: 400 Bad Request"