//array que definen en el estilos.css el tamaño de la letra y el índice
var classes = ["f0", "f1", "f2", "f3", "f4", "f5", "f6"];
var classIndex = 2;

//manejador de eventos que se encargan de asociar las funcionalidades a los botones, en este caso aumentar tamaño
document.getElementById('aumentar').addEventListener('click', function () {
    let previousClass = classIndex;
    classIndex++;
    classIndex = (classIndex == classes.length) ? classes.length - 1 : classIndex;
    changeClass(previousClass, classIndex);
});

//manejador de eventos que se encargan de asociar las funcionalidades a los botones, en este caso disminuir tamaño
document.getElementById('disminuir').addEventListener('click', function () {
    let previousClass = classIndex;
    classIndex--;
    classIndex = (classIndex < 0) ? 0 : classIndex;
    changeClass(previousClass, classIndex);
});

//funcion que sirve para comprobar que el nombre de la clase ha cambiado
function changeClass(previous, next) {
    if (previous != next) {
        var htmlElement = document.querySelector('html')
        htmlElement.classList.remove(classes[previous]);
        htmlElement.classList.add(classes[next]);
    }
}