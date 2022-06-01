// Validar formulario de los campos de empleado

// Funcion que sirve para definir si un telefono teien la longitud idenea o no, en caso de que no sea correcto se escribira un mensaje
function addItemtel(event) {

    let telefono = document.getElementById("id_telefono");
    let longitud = event.currentTarget.value.length;
    let principal = document.getElementById("parrafoerrortelefono");
    
        if(longitud != 9){
            principal.textContent = "Longitud del telefono erronea(se necesitan 9 números.)";
            return
        }
        if(longitud == 9){
            principal.textContent = "";
            return
        }

}

// Funcion para comprobar que en el campo nombre no hay caracteres especiales, en caso de que asi sea se escribira un mensaje
function addItem(event) {
    let nombre = document.getElementById("nombre");
    let valor = event.currentTarget.value
    let parrafo = document.getElementById("parrafoerrornombre");
    
        if(valor.includes('$') || valor.includes('%')|| valor.includes('&') || valor.includes('#') || valor.includes('1') || valor.includes('3') || valor.includes('2') || valor.includes('4') || valor.includes('5') || valor.includes('6') || valor.includes('7') || valor.includes('8') || valor.includes('9')|| valor.includes('0') ){
            parrafo.textContent = "No se pueden escribir ni numeros ni puntuacion especial($,%,&,#)";
            return
        }else{
            parrafo.textContent = "";
            return
        }
       
}


// Funcion para comprobar si hay algun error en los campos anteriores, en caso de que no fuese asi se añadiria el registro
function error(event){
    event.preventDefault();
    if (location.href = 'http://127.0.0.1:8000/appDeustotil/clientes/create/'){
        let principal = document.getElementById("parrafoerrortelefono");
        let parrafo = document.getElementById("parrafoerrornombre");
            if(principal.textContent != "" || parrafo.textContent != ""  ){
                return;
            }else{
                this.submit();
            }
    }
}


/* AÑADIR CONTROLADORES */

// Controlador, para detectar lo que va escribiendo en el campo telefono
let tel = document.getElementById("id_telefono");
tel.addEventListener("keyup", addItemtel)  
  
// Controlador, para detectar lo que va escribiendo en el campo nombre
let nom = document.getElementById("nombre");
nom.addEventListener("keyup", addItem);

// Controlador que detecta cuando hemos pulsado el boton
let boton = document.getElementById("botonFormulario");
boton.addEventListener("submit", error);
