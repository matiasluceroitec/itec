//Declaro el contador como un elemento de la localStorage
let counter = localStorage.getItem('megusta');

document.getElementById('likes').textContent = "likes :" + counter;

//Si la localStorage esta vacia, inicio con likes:0
if (localStorage.getItem('megusta') == null) {
    document.getElementById('likes').textContent = "likes :0";
}

//let likes=document.getElementById('likes').textContent;

document.getElementById('incrementa').onclick = function () {
    aumentar();
}

document.getElementById('disminuye').onclick = function () {
    disminuir();
}

document.getElementById('resetear').onclick = function () {
    resetea();
}

function aumentar() {
    counter++;
    render();
    save();
}

function disminuir() {
    counter--;
    render();
    save();
}

function resetea() {
    counter = 0;
    render();
    save();
}

function save() {
    localStorage.setItem('megusta', counter);
}

function render() {
    document.getElementById('likes').innerHTML = "likes :" + counter;
}