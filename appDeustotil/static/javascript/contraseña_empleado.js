// Controlador que controla los caracteres que se van escribiendo en el nombre 
var nombre = document.getElementById('nombre')
nombre.addEventListener("keyup", generaContraseña)

// Controlador que controla los caracteres que se van escribiendo en el contraseña
var contraseña = document.getElementById('contraseña')
contraseña.addEventListener("keyup", generaContraseña)

// Controlador que controla los caracteres que se van escribiendo en el dni
var dni = document.getElementById('dni')
dni.addEventListener("keyup", generaContraseña)

// Funcion que va generando una contraseña de forma automatica, cogiendo los 3 primeros caracteres, invirtiendolos y poniedno a continuacion los 3 primeros digitos del DNI
function generaContraseña(event){
    event.preventDefault()
    var substrNombre = nombre.value.substring(nombre.value.length-4)
    var subInvNombre = invertirCadena(substrNombre)
    var subsdni = dni.value.substring(-1, 3)

    contraseña.setAttribute('value', subInvNombre + subsdni)
}

// Funcion que invierte los carcetres de una cadena
function invertirCadena(cad) {
    return cad.split("").reverse().join("");
}