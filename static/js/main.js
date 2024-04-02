(function ($) {
    "use strict";

    // Initiate the wowjs
    new WOW().init();


    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Handle Edit Button Click
document.addEventListener('click', function () {
    const editButtons = document.querySelectorAll('.edit-child-btn');

    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const childId = this.dataset.childId;
            const editModal = document.getElementById('editModal');
            
            // Update the edit modal's content with a loading indicator
            editModal.querySelector('.modal-body').innerHTML = '<div>Loading...</div>';

            // Fetch the edit modal content directly from the server using a normal form submission
            fetch(`/edit_child/${childId}`)
                .then(response => response.text())
                .then(data => {
                    // Update the edit modal's content with the fetched HTML
                    editModal.querySelector('.modal-body').innerHTML = data;
                })
                .catch(error => console.error('Error fetching edit modal content:', error));
        });
    });
});


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            992: {
                items: 2
            }
        }
    });

})(jQuery);

// Limit the checkbox selected up to 4
function limitCheckboxSelection() {
    var checkboxes = document.getElementsByName("child_choice");
    var checkedCount = 0;

    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkedCount++;
        }
    }

    if (checkedCount >= 4) {
        for (var i = 0; i < checkboxes.length; i++) {
            if (!checkboxes[i].checked) {
                checkboxes[i].disabled = true;
            }
        }
    } else {
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].disabled = false;
        }
    }
}

// Function to hide flash messages after 3sec.
setTimeout(function () {
    let Flash_messages = document.getElementById('messages');
    if (Flash_messages) {
        Flash_messages.style.display = 'none';
    }
}, 3000);

// 
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});
