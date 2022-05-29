var nombre = document.getElementById('nombre')
nombre.addEventListener("keyup", generaContraseña)

var contraseña = document.getElementById('contraseña')
contraseña.addEventListener("keyup", generaContraseña)

var dni = document.getElementById('dni')
dni.addEventListener("keyup", generaContraseña)

function generaContraseña(event){
    event.preventDefault()
    var substrNombre = nombre.value.substring(nombre.value.length-4)
    var subInvNombre = invertirCadena(substrNombre)
    var subsdni = dni.value.substring(-1, 3)

    contraseña.setAttribute('value', subInvNombre + subsdni)
}

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