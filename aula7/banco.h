#ifndef BANCO_H
#define BANCO_H

#include "conta.h"

class Banco
{
private:
    Conta *contas;
    int top;
    int senhaFuncionario;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero);
    void atendimentoCliente();
    void atendimentoFuncionario();
    void adicionaConta(int senha, int numero, std::string titular, std::string tipo, double saldo);
    bool removeConta(int numero);
};


#endif
