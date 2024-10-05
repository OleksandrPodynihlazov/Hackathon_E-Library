// Get the button and popup elements
const notificationButton = document.getElementById('notificationButton');
const notificationPopup = document.getElementById('notificationPopup');

// Add click event listener to the button
notificationButton.addEventListener('click', () => {
    // Toggle the 'show' class to display/hide the popup
    notificationPopup.classList.toggle('show');
});

// Close the popup if clicked outside
document.addEventListener('click', function (event) {
    const isClickInside = notificationButton.contains(event.target) || notificationPopup.contains(event.target);
    
    if (!isClickInside) {
        notificationPopup.classList.remove('show');
    }
});
