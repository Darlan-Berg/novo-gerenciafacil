objs = {
    "lista": [
        {
            "a": 1,
            "b": 2,
            "c": 3,
            "atributo": null
        },
        {
            "d": 4,
            "e": 5,
            "f": 6,
            "atributo": null
        }
    ]
}

console.log(objs)
lista = objs.lista
console.log(lista)

for (i=0; i<lista.length; i++) {
    lista[i].atributo = "Olá"
}

console.log(objs)
console.log(lista)