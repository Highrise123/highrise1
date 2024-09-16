function handleFeedback(isPositive) {
    const form = document.getElementById('feedbackForm');
    const formData = new FormData(form);
    const queryParams = new URLSearchParams(formData).toString();
    if (isPositive) {
        // Redirect to the specific Google Review page
        window.location.href = 'https://search.google.com/local/writereview?placeid=ChIJA7Zo0DFxqDsRmk9BBAmeXN8';
    } else {
        // Redirect to negative feedback page with form data as query parameters
        window.location.href = `/feedback?${queryParams}`;
    }
}
