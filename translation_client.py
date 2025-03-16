# Prompt Comment to generate this file:
# Create a Python script that defines a function to translate text using an API.
# The function should:
# 1. Accept the text to be translated and the target language as parameters.
# 2. Construct a prompt that instructs the API to translate the text without adding any extra context.
# 3. Build a JSON payload using the model "gemma3:1b" and include the constructed prompt.
# 4. Send a POST request to the API endpoint at "http://localhost:11434/api/generate" with the appropriate headers.
# 5. Return the translated text from the API response if the HTTP status code is 200, or an error message otherwise.


import requests

def translate_text(text, target_language):
    # Costruzione del prompt a partire dal testo e dalla lingua di destinazione.
    prompt = f"Translate to {target_language}: {text}, don't add any context."
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['response']
    else:
        # In caso di errore si restituisce un messaggio di errore.
        return f"Error: {response.status_code} {response.text}"
    
