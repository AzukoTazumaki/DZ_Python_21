/* PRELOADER */
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
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
})(jQuery)