
function addItemtel(event) {

    let telefono = document.getElementById("id_telefono");
    let longitud = event.currentTarget.value.length;
    let principal = document.getElementById("parrafoerrortelefono");
    
        if(longitud != 9){
            principal.textContent = "Longitud del telefono erronea(se necesitan 9 números.)";
            return
        }
        if(longitud == 9){
            principal.textContent = " ";
            return
        }


    
    telefono.value = "";
  }

function addItem(event) {
    let nombre = document.getElementById("id_nombre");
    let valor = event.currentTarget.value
    let parrafo = document.getElementById("parrafoerrornombre");
    
        if(valor.includes('$') || valor.includes('%')|| valor.includes('&') || valor.includes('#') || valor.includes('1') || valor.includes('3') || valor.includes('2') || valor.includes('4') || valor.includes('5') || valor.includes('6') || valor.includes('7') || valor.includes('8') || valor.includes('9')|| valor.includes('0') ){
            console.log('hola')
            parrafo.textContent = "No se pueden escribir ni numeros ni puntuacion especila($,%,&,#)";
            return
        }else{
            parrafo.textContent = " ";
            return
        }
       

}
 
  function error(event){
    event.preventDefault();
    let principal = document.getElementById("parrafoerrortelefono");
    let parrafo = document.getElementById("parrafoerrornombre");
    let parrafo1 = document.getElementById("parrafoerroremail");
        if(principal.textContent != "" || parrafo.textContent != "" || parrafo1.textContent != "" ){

            return;
        }
    this.submit();
  }

  /* AÑADIR CONTROLADORES */
  let tel = document.getElementById("id_telefono");
  tel.addEventListener("keyup", addItemtel)  
  let nom = document.getElementById("id_nombre");
  nom.addEventListener("keyup", addItem);
//  tel.addEventListener("keyup", userWarning);

  let boton = document.getElementById("formulario");
  boton.addEventListener("submit", error)

