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

document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
        item.addEventListener('click', function() {
            console.log(1)
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');
        });
    });
});
