
$(document).ready(function(){
    $("#cont_registro").fadeOut();

    $("#link_registro").click(function(){
        $("#cont_login").fadeOut();
        $("#cont_registro").fadein();
     
    })
    $("#link_login").click(function(){
       
        $("#cont_login").fadeIn();
       
        $("#cont_registro").fadeOut();
    })

$("#cont_img").mouseleave(function(){
    $("#detalle_img").fadeOut();
})
$("#cont_img").mouseenter(function(){
    $("#detalle_img").fadeIn();
})


})
//$("#cont_registro").slideUp();
//$("#cont_login").slideDown();
//$("#cont_login").slideUp();
//$("#cont_registro").slideDown();