#ifndef BANCO_H
#define BANCO_H

#include "conta.h"

class Banco
{
private:
    Conta *contas;//Cria um vetor de objetos do tipo Conta que pode armazenar até 100 contas
    int top;
    int senhaFuncionario;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero); //Metodo que retorna o endereço do objeto conta que possui o mesmo numero informado
    void atendimentoCliente();
    void atendimentoFuncionario();
    void adicionaConta(int senha, int numero, std::string titular, std::string tipo, double saldo);
    bool removeConta(int numero);
};


#endif