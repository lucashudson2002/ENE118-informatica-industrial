# Aula 12 - Atividades Complementares

Crie uma aplicação cliente-servidor com as seguintes características:

<ol>
    <li> O cliente deverá enviar para o servidor uma imagem.
    <li> O servidor deverá aplicar uma técnica de reconhecimento de faces e, caso haja uma face na imagem, deverá criar um retângulo azul ao redor da face.
    <li> Após realizado o processamento, o servidor deverá enviar a imagem processada para o cliente.
    <li> O cliente deverá mostrar a imagem processada.
</ol>

Dicas:
- Estude o código [‘Aula11/ExemploProcessamentoImagem’](https://github.com/Pguilhermem/InformaticaIndustrialUFJF/tree/main/Python/Aula%2011/ExemploProcessamentoImagem);
- A comunicação entre cliente e servidor deve considerar que um dos agentes enviará primeiro o tamanho da imagem (em bytes) para que o outro saiba a quantidade de dados a ser recebida.