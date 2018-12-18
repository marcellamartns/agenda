function atualizar() {
    var nome = document.getElementById("nomecontato").value;
    var telefone = document.getElementById("telefone").value;
    var email = document.getElementById("email").value;
    var complemento = document.getElementById("complemento").value;
    var idContato = document.getElementById("idContato").value;

    var metodo = "post";

    var dados = {nome:nome,
        telefone:telefone,
        email:email,
        complemento:complemento
    };

    console.log(dados);

    if (idContato !== "0")
        metodo = "put";
    fetch("/contato/"+idContato, {
        method: metodo,
        body:JSON.stringify(dados)
    })
    alert("Contato atualizado!")
}



function deletar(){

    decisao = confirm("Excluir contato?");
    if (decisao) {
        console.log("teste")
        var idContato = document.getElementById("idContato").value;
        console.log(idContato);
        fetch("/contato/"+idContato, {
            method:"delete"
        });
    }
}


function teste(){

    decisao = confirm("Clique em um botão!");

    if (decisao){

        alert ("Você clicou no botão OK,\n"+

        "porque foi retornado o valor: "+decisao);

    } else {

        alert ("Você clicou no botão CANCELAR,\n"+

        "porque foi retornado o valor: "+decisao);

    }
}