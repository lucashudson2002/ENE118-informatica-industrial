#ifndef BANCO_H
#define BANCO_H

#include "conta.h"

#define NUMCONTAS 100 //Define que a palavar NUMCONTAS passa a valer como escrever 100

class Banco
{
private:
    Conta contas[NUMCONTAS];//Cria um vetor de objetos do tipo Conta que pode armazenar até 100 contas
    int quantidade;
    int senhaFuncionario;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero); //Metodo que retorna o endereço do objeto conta que possui o mesmo numero informado
    void atendimentoCliente();
    void atendimentoFuncionario();
    bool adicionaConta(int senha, int numero, std::string titular, std::string tipo, double saldo);
};


#endif