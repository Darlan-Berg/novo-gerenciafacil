const promessa = new Promise((resolve, reject) => {

    const usuario = "Darlan" // essa variavel representa os dados que sao recebidos em uma requisicao

    if (usuario === "Darlan") {
        resolve("Olá, Darlan!")
    } else {
        reject("Ué!? Cadê o Darlan!?")
    }
});

promessa.then((data) => { // data e o retorno do resolve ou do reject
    console.log(data)     // os thens sao usados para descascar as promessas
});



// ENCADEAMENTO DE thens
const promessa2 = new Promise((resolve, reject) => {

    const usuario = "Dorimê"

    if (usuario === "Dorimê") {
        resolve("Olá, Dorimê!")
    } else {
        reject("Ué!? Cadê o Dorimê!?")
    }
});

// o then e usado quando o resolve retorna uma resposta
promessa2.then((respostaDoResolve) => {
    return (respostaDoResolve + " Manipulação do primeiro then.")
}).then((respostaDoResolveModificada) => {
    console.log(respostaDoResolveModificada + " Manipulação do segundo then.")
});



// USANDO O catch
const promessa3 = new Promise((resolve, reject) => {

    const usuario = "Fulano"

    if (usuario === "Juriscleybison") {
        resolve("Olá, Juriscleybison!")
    } else {
        reject("Mostre onde está o Juriscleybison!")
    }
});

promessa3.then((data) => {
    console.log(data)
}).catch((respostaDoReject) => {
    console.log("Ocorreu um erro: " + respostaDoReject)
});