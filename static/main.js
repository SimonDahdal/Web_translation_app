// Prompt Comment: 
// This file handles the translation form submission. 
// It listens for the "submit" event on the form with id "translateForm", prevents the default browser behavior,
// collects user input for the text to translate and the target language, 
// and sends a POST request to the '/translate' endpoint.
// Once a JSON response is received, 
// it displays the translated text or an error message in the element with id "result".
// It also handles any network errors by logging them to the console.


// Listen for the form's "submit" event
document.getElementById('translateForm').addEventListener('submit', function(event) {
    // Prevent default form submission behavior
    event.preventDefault();
    
    // Gather input values
    const text = document.getElementById('text').value;
    const target_language = document.getElementById('target_language').value;

    // Send a POST request to the "/translate" endpoint
    fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, target_language: target_language })
    })
    .then(response => response.json()) // Parse response as JSON
    .then(data => {
        // Display the translated text or error message
        document.getElementById('result').innerText = data.translated_text || data.error;
    })
    // Handle any network errors
    .catch(error => console.error('Error:', error));
});