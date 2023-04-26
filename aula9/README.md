## Aula 9 - Desafio

- Crie uma classe abstrata <strong> MobileRobot</strong>. Esta classe deve possuit o seguinte atributo e a seguinte função-membro:

<ul type=square>
    <li> double PosicaoAtual[3]; <font color="green">// X, Y e Z</font> 
    <li> double getPosicaoAtual(char coordenada);
    <li> void setPosicaoAtual(double X, double Y, double Z);
    <li> <strong> virtual </strong> void Mover(double Xvel, double Yvel, double Zvel, double
tempo) =0;
</ul>

- Crie as classes derivadas RoboTerrestre e Quadrotor;

- Faça a implementação da função <strong> Mover </strong> de modo que o robô se mova e atualize a posição atual conforme os parâmetros da função.

- A função mover deverá imprimir na tela:

<ul type=square>
    <li> A tarefa: “Acionando hélices...” para o <strong> Quadrotor </strong> e “Acionando os
motores das rodas...” para o <strong> RoboTerrestre </strong>;
    <li> A posição antes do movimento;
    <li> A posição depois do movimento.
</ul>

- <strong>Não se esqueça dos construtores! </strong>

- Lembre-se: Robô terrestre possui posição Z=0 para todos os casos.

- Crie uma outra função no arquivo
main.cpp:

<strong> ExecutaMovimento(MobileRobot *ptr) </strong>

- Esta função deverá receber o ponteiro dos
objetos e executar um movimento com
velocidades aleatórias em um tempo aleatório.

As velocidades e o tempo “sorteados” deverão ser
impressos na tela.