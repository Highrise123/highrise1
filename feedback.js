document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('negativeFeedbackForm');
    const thankYouMessage = document.getElementById('thankYouMessage');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const feedbackData = Object.fromEntries(formData.entries());
        feedbackData.improvementAreas = formData.getAll('improvementAreas');
        
        console.log('Submitting negative feedback:', feedbackData);
        showThankYouMessage();
    });

    function showThankYouMessage() {
        form.style.display = 'none';
        thankYouMessage.style.display = 'block';
    }
});
