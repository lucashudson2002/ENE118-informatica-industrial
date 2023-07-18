# Aula 13 - Atividade Complementar

- O protocolo MODBUS foi concebido originalmente para possibilitar a transmissão apenas de dados inteiros de 16 bits ou de dados binários. No entanto, a partir da concatenação de 2 ou mais registradores, é possível realizar a comunicação utilizando dados mais complexos como floats e strings. Esta funcionalidade normalmente é disponibilizada em boa parte das bibliotecas desenvolvidas para a comunicação através do protocolo MODBUS.

- Desta forma, explore a documentação da biblioteca PyModbus e aprimore o servidor e o cliente desenvolvidos de modo que seja possível transmitir dados complexos. Os dados que deverão ser lidos e escritos são:

<ul type=square>
    <li> floats (dica: use as classes BinaryPayloadBuilder e BinaryPayloadDecoder)
    <li> Holding Registers como bits individuais.
    <ul>
        <li> Dica leitura: i) ler o registrador; ii) converter para uma lista com 16 posições, em que cada posição representa um bit; iii) mostrar a lista de bits.
        <li> Dica escrita: i) realizar a leitura conforme o procedimento acima; ii) alterar o bit desejado; iii) converter a lista para inteiro; iv) escrever no registrador.
    </ul>
</ul>