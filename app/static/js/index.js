$(function() {
    $("#menu-toggle").click(function(e) {
        e.preventDefault()
        $("#wrapper").toggleClass("toggled")
    })

    var timer
    $(window).on('mousemove', function() {
        $('.navbar').addClass('show')
        $('.panel-wrapper, .panel-primary').addClass('down')
        try {
            clearTimeout(timer)
        } catch (e) {}
        timer = setTimeout(function() {
            $('.navbar').removeClass('show')
            $('.panel-wrapper, .panel-primary').removeClass('down')
        }, 3000)
    })
})
