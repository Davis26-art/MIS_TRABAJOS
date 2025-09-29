// -----------------------------------------
// Ejercicio 96: Manipulador de Archivos
// -----------------------------------------
// Simula operaciones básicas con archivos usando arrays.

// Array que almacena los "archivos"
let archivos = [];

// Función para crear un archivo
function crearArchivo(nombre) {
    archivos.push(nombre); // agrega el nombre del archivo al array
    console.log("Archivo creado:", nombre);
}

// Función para listar todos los archivos
function listarArchivos() {
    console.log("Archivos:", archivos);
}

// Función para eliminar un archivo por nombre
function eliminarArchivo(nombre) {
    let index = archivos.indexOf(nombre); // busca la posición del archivo
    if (index !== -1) {
        archivos.splice(index, 1); // elimina el archivo del array
        console.log("Archivo eliminado:", nombre);
    } else {
        console.log("Archivo no encontrado");
    }
}

// Uso de las funciones
crearArchivo("nota.txt");   // agrega "nota.txt"
crearArchivo("tarea.doc");  // agrega "tarea.doc"
listarArchivos();           // muestra ["nota.txt", "tarea.doc"]
eliminarArchivo("nota.txt"); // elimina "nota.txt"
listarArchivos();           // muestra ["tarea.doc"]
