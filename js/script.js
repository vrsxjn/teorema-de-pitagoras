const buttonEnvia = document.querySelector("#send"); //Trazendo o botão "Calcular" para dentro do arquivo script.js.

async function ladoC(ladoA, ladoB) { //Criando uma função async para facilitar o request dentro da api.
  const resposta = await axios.get(`http://127.0.0.1:5000/?ladoa=${ladoA}&ladob=${ladoB}`)//Fazendo um request diretamente para api usando axios.
  document.getElementById('ladoC').innerHTML = `C:${resposta.data.result}`//Alterando o valor do "c" de acordo com o resultado retornado da api.
}

buttonEnvia.addEventListener("click", function(e) { //Função de captação de click dentro do botão "Calcular".
  e.preventDefault(); //Trazendo o preventDefault para impedir que o evento ocorra sem necessidade.
    
  const ladoA = document.querySelector("#ladoA"); //Trazendo o resultado fornecido dentro do imput do html ladoA.
  const ladoB = document.querySelector("#ladoB"); //Trazendo o resultado fornecido dentro do imput do html ladoB.
  const valorA = ladoA.value; //Filtrando o retorno para coletar somente do valor fornecido do usuário.
  const valorB = ladoB.value;

  ladoC(valorA,valorB) //Trazendo a função criada para fazer o request com os parâmentros informados no "index.html".
})