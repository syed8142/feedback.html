document.getElementById('feedbackForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from submitting normally

    const form = event.target;
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            form.reset(); // Clear the form
            document.getElementById('thankYouMessage').classList.remove('hidden');
        } else {
            alert('There was an issue submitting your feedback. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});
