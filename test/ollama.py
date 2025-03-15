import requests

# Define the URL
url = "http://localhost:11434/api/generate"

# Define the JSON payload
payload = {
    "model": "gemma3:1b",
    "prompt": "Why is the sky blue? short answer",
    "stream": False }

# Define the headers
headers = { "Content-Type": "application/json" }

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print(response.json()['response'])
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

