//$.validator.addMethod("terminarPor", function(value, element,parametro){
//} )
//

$(#formulario_cont).validate({
    rules:{
        nombre:{
            required:true,
        minlength: 3,
        maxlength: 30
        }
        email:{
        required:true,
        email:true

        }
        mensaje:{
        required:true,
        minlength: 5,
        maxlength: 200
        }
    }
})

$("guardar").click(function(){
    if($("#formulario_cont").valid() == false){
        return;
    }
    let nombre = $("#nombre").val()
    let email = $("#mail").val()
    let mensaje = $("#mensaje").val()

    

})