$(function() {
    // toggle sidebar
    $("#menu-toggle").click(function(e) {
        e.preventDefault()
        $("#wrapper").toggleClass("toggled")
    })

    // navbar hidden-show
    var timer
    $('#nav-wrapper').on('mouseover', function() {
        $('.navbar').addClass('show')
        $('.panel-wrapper, .panel-primary').addClass('down')
        try {
            clearTimeout(timer)
        } catch (e) {}
        timer = setTimeout(function() {
            $('.navbar').removeClass('show')
            $('.panel-wrapper, .panel-primary').removeClass('down')
        }, 2000)
    })
})

