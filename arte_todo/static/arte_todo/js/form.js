
$(document).ready(function(){


$("#detalle_img").hide();


$("#cont_img").mouseleave(function(){
    $("#detalle_img").slideUp();
})
$("#cont_img").mouseenter(function(){
    $("#detalle_img").slideDown();
})
})
