// EXERCISE ABOUT ARRAYS

var command = null;
var lista = [];
var theName = null;

while (command != "quit") {
    command = prompt("What would you like to do? Options: add, remove, display, quit?")
    if (command === 'add') {
        theName = prompt("Introduce the name of the student that will be added to the class:")
        lista.push(theName)
    } else if (command === 'remove') {
        theName = prompt("Introduce the name of the student that will be removed from the class:")
        var i = lista.indexOf(theName)
        if (i !== -1) {
            lista.splice(i, 1)
        }
    } else if (command === 'display') {
        console.log(lista)
    } else if (command === 'quit') {
        break
    } else {
        alert('The command requested is not among the options.')
    }
}