
$(document).ready(function(){
    $("#cont_registro").fadeOut();

    $("#link_registro").click(function(){
        $("#cont_login").slideDown();
        $("#cont_login").fadeOut();
        $("#cont_registro").fadein();
        $("#cont_registro").slideUp();
    })
    $("#link_login").click(function(){
        $("#cont_login").slideUp();
        $("#cont_login").fadeIn();
        $("#cont_registro").slideDown();
        $("#cont_registro").fadeOut();
    })

$("#cont_img").mouseleave(function(){
    $("#detalle_img").fadeOut();
})
$("#cont_img").mouseenter(function(){
    $("#detalle_img").fadeIn();
})


})
