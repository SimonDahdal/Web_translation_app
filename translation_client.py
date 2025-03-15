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