import { mostrarStatusDaOperacao } from "./index.js";

const form = document.getElementById("formVendaProdutos")
form.addEventListener("submit", (event) => {
    event.preventDefault() // se essa linha for apagada havera um erro

    // coletar dados do form
    const nome = document.getElementById("nome").value
    const marca = document.getElementById("marca").value
    const qtd = parseInt(document.getElementById("qtd").value)

    // fazer requisicao para o servidor e buscar o arquivo estoque.json
    fetch("/retornar-estoque") // o fetch retorna um objeto Response do javascript
    .then((objDeResponse) => {
        return objDeResponse.json() // retorna o objeto javascript/json que esta no corpo da requisicao
    })
    .then((objJavaScript) => {
        const estoque = objJavaScript.listaProdutos

        for (let i = 0; i < estoque.length; i++) {
            const produto = estoque[i]

            // verificar se o produto esta em estoque
            if (produto.nome.toLowerCase() === nome.toLowerCase() && produto.marca.toLowerCase() === marca.toLowerCase()) {
                // verificar quantidade a ser vendida
                if (qtd <= parseInt(produto.qtd)) {
                    // fazer requisicao para o servidor e atualizar estoque
                    produto.qtd -= qtd

                    fetch("/remover-produto-do-json", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(objJavaScript)
                    })
                    mostrarStatusDaOperacao("Venda realizada com sucesso.")
                } else if (qtd > parseInt(produto.qtd)) {
                    const mensagem = `Não foi possível efetuar a venda. Não há quantidade suficiente de "${produto.nome}" da marca "${produto.marca}" em estoque.`
                    mostrarStatusDaOperacao(mensagem)
                }
            } else if (produto.nome.toLowerCase() === nome.toLowerCase() && produto.marca.toLowerCase() !== marca.toLowerCase()) {
                const mensagem = `O produto "${nome}" está disponível em estoque, porém apenas de outra marca.`
                mostrarStatusDaOperacao(mensagem)
            }
        }

    })
    .catch((erro) => {
        console.log("Algo deu errado ao fazer a requisição do estoque. Descrição do erro: " + erro)
    })
});