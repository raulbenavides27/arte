
$(document).ready(function(){
    $("#cont_registro").hide();
    $("#cont_login").fadeIn();
    $("#link_registro").click(function(){
        $("#cont_login").fadeOut();
        $("#cont_registro").show();
     
    })
    $("#link_login").click(function(){
        $("#cont_login").fadeIn();
        $("#cont_registro").fadeOut();
    })

    $("#btn-iniciar").click(function(){
        alert(text("Usuario no registrado"));
    })


$("#detalle_img").hide();
$("#detalle_img1").hide();
$("#detalle_img2").hide();
$("#detalle_img3").hide();
$("#detalle_img4").hide();
$("#detalle_img5").hide();
$("#cont_img").mouseleave(function(){
    $("#detalle_img").slideUp();
})
$("#cont_img").mouseenter(function(){
    $("#detalle_img").slideDown();
})

$("#cont_img1").mouseleave(function(){
    $("#detalle_img1").slideUp();
})
$("#cont_img1").mouseenter(function(){
    $("#detalle_img1").slideDown();
})
$("#cont_img2").mouseleave(function(){
    $("#detalle_img2").slideUp();
})
$("#cont_img2").mouseenter(function(){
    $("#detalle_img2").slideDown();
})
$("#cont_img3").mouseleave(function(){
    $("#detalle_img3").slideUp();
})
$("#cont_img3").mouseenter(function(){
    $("#detalle_img3").slideDown();
})
$("#cont_img4").mouseleave(function(){
    $("#detalle_img4").slideUp();
})
$("#cont_img4").mouseenter(function(){
    $("#detalle_img4").slideDown();
})
$("#cont_img5").mouseleave(function(){
    $("#detalle_img5").slideUp();
})
$("#cont_img5").mouseenter(function(){
    $("#detalle_img5").slideDown();
})
})
