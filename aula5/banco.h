#ifndef BANCO_H
#define BANCO_H

#include "conta.h"

#define NUMCONTAS 100

class Banco
{
private:
    Conta contas[NUMCONTAS];
    int quantidade;
    int senhaFuncionario;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero);
    void atendimentoCliente();
    void atendimentoFuncionario();
    bool adicionaConta(int senha, int numero, std::string titular, std::string tipo, double saldo);
};


#endif
