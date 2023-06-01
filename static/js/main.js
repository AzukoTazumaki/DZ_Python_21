/* PRELOADER */
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.querySelector("body").classList.add("loaded");
    }, 500)
  });

/* SCROLLBAR */
(function ($) {
    $(window).on("load", function () {
        $('body').mCustomScrollbar({
            theme: "inset-3-dark",
            autoHideScrollbar: true,
            mouseWheel: {
                deltaFactor: 8,
                normalizeDelta: false
            },
            scrollButtons: {
                enable: true
            }
        });
    });
})(jQuery);

/* CUSTOM INPUT MASK */
const InputMask = require('inputmask');
const phone_input = document.getElementById('employee_phone_number');
let phone = new InputMask('+7(928)-555-55-55');
phone.mask(phone_input);