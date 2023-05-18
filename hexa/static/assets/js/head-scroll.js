$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    var box = $('#top').height();
    var header = $('header').height();

    if (scroll >= box - header) {
        $("header").addClass("background-header");
        $(".mc-up_header").css("display", "none");
        $(".header-area.header-sticky").css("min-height", "80px");
        $(".header-area").css("height", "100px");
    } else {
        $("header").removeClass("background-header");
        $(".mc-up_header").css("display", "block");
        $(".header-area.header-sticky").css("min-height", "145px");
        $(".header-area").css("height", "145px");
    }
});

$(window).resize(function() {
    $("header").removeClass("background-header");
    $(".mc-up_header").css("display", "block");
    $(".header-area.header-sticky").css("min-height", "145px");
    $(".header-area").css("height", "145px");
});

$(window).scroll(function() {
    if ($(window).scrollTop() == 0) {
        $("header").removeClass("background-header");
        $(".mc-up_header").css("display", "block");
        $(".header-area.header-sticky").css("min-height", "145px");
        $(".header-area").css("height", "145px");
    }
});