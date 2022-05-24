const imagen1= document.getElementById('imagen1');
const imagen2= document.getElementById('imagen2');
const imagen3= document.getElementById('imagen3');

const cargarImagen = (entradas,observador) => {
    
    entradas.forEach((entrada) => {
        if(entrada.isIntersecting){
            console.log('la imagen esta en el viewport')
        }
    });
}

const observador = new IntersectionObserver(cargarImagen,{
    root: null,
    rootMargin:'0px 0px 0px 0px',
    threshold:1.0 
});
observador.observe(imagen1);
observador.observe(imagen2);
observador.observe(imagen3);