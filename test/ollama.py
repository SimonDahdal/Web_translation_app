import pytest
import requests
from unittest.mock import patch, MagicMock

def test_ollama_endpoint():
    with patch("requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": "Sky is blue due to Rayleigh scattering"}
        mock_post.return_value = mock_response

        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "gemma3:1b",
            "prompt": "Why is the sky blue? short answer",
            "stream": False
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)

        assert response.status_code == 200
        assert len(response.json()["response"]) > 0
        mock_post.assert_called_once_with(url, json=payload, headers=headers)
