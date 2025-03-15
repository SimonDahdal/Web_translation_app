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