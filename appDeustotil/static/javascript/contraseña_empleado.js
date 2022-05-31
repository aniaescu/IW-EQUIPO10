//controlador que controla los caracteres que se van escribiendo en el nombre 
var nombre = document.getElementById('nombre')
nombre.addEventListener("keyup", generaContraseña)

//controlador que controla los caracteres que se van escribiendo en el contraseña
var contraseña = document.getElementById('contraseña')
contraseña.addEventListener("keyup", generaContraseña)

//controlador que controla los caracteres que se van escribiendo en el dni
var dni = document.getElementById('dni')
dni.addEventListener("keyup", generaContraseña)

// funcion que va generando una contraseña de forma automatica, cogiendo los 3 primeros caracteres, invirtiendolos y poniedno a continuacion los 3 primeros digitos del DNI
function generaContraseña(event){
    event.preventDefault()
    var substrNombre = nombre.value.substring(nombre.value.length-4)
    var subInvNombre = invertirCadena(substrNombre)
    var subsdni = dni.value.substring(-1, 3)

    contraseña.setAttribute('value', subInvNombre + subsdni)
}

//funcion que invierte los carcetres de una cadena
function invertirCadena(cad) {
    return cad.split("").reverse().join("");
}

//var botonLogin = document.getElementById('botonLogin')
//botonLogin.addEventListener("click", borrarCampos)
//botonLogin.addEventListener("click", limpiarFormulario)

//function borrarCampos(event){
//    event.preventDefault()
//    document.getElementsByTagName('input').reset()
//}

//function limpiarFormulario(event) {
//    event.preventDefault()
//    document.getElementById("id_login_form").reset();
//  }