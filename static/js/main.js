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


// populate the form with child details when the modal is shown
document.addEventListener('DOMContentLoaded', function () {
    var staticBackdrop = document.getElementById('staticBackdrop');
    staticBackdrop.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var childfname = button.getAttribute('data-childfname');
        var childlname = button.getAttribute('data-childlname');
        var date_of_birth = button.getAttribute('data-date_of_birth');
        var school_name = button.getAttribute('data-school_name');
        var school_year = button.getAttribute('data-school_year');
        var child_choice = button.getAttribute('data-child_choice').split(',');
        var child_med_conditions = button.getAttribute('data-child_med_conditions');

        // Update the form action with the correct kids_id 
        var form = document.getElementById('editForm');
        form.action = "/edit_child/" + id;

        // Populate the form fields with the child details
        document.getElementById('childfname').value = childfname;
        document.getElementById('childlname').value = childlname;
        document.getElementById('date_of_birth').value = date_of_birth;
        document.getElementById('school_name').value = school_name;
        document.getElementById('school_year').value = school_year;

        // Check the appropriate checkboxes for child_choice
        var checkboxes = document.querySelectorAll('#child_choice .form-check-input');
        checkboxes.forEach(function (checkbox) {
            checkbox.checked = child_choice.includes(checkbox.value);
        });

        // Populate the child_med_conditions textarea
        document.getElementById('child_med_conditions').value = child_med_conditions;
    });
});

// Function to hide flash messages after 3sec.
setTimeout(function () {
    let Flash_messages = document.getElementById('messages');
    if (Flash_messages) {
        Flash_messages.style.display = 'none';
    }
}, 3000);

// tooltip
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});
