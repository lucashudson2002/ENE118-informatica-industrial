#include "banco.h"
#include <iostream>

using namespace std;

Banco::Banco()
{
    this->senhaFuncionario = 246810;
    this->contas[0] = Conta(1234, 1, "Joao", "Corrente", 300);
    this->contas[1] = {4567, 2, "Jose", "Poupanca", 800};
    this->contas[2] = {7890, 3, "Maria", "Corrente", 1000};
    this->contas[3] = {8956, 4, "Madalena", "Poupanca", 2000};
    this->quantidade = 4;
}

Banco::~Banco()
{
}

Conta *Banco::buscaConta(int numero)
{
    for (int i = 0; i < NUMCONTAS; i++)
    {
        if (numero == this->contas[i].numero)
        {
            return &this->contas[i];
        }
    }

    return nullptr;
}

void Banco::atendimentoCliente()
{
    Conta *contaCliente;
    int numC = 0;
    int senhain;
    bool atendimento = true;

    cout << "Bem vindo ao sistema de atendimento do banco" << endl;
    cout << "Digite o numero da sua conta: ";
    cin >> numC;

    contaCliente = this->buscaConta(numC);

    if (contaCliente == nullptr)
    {
        cout << "Conta invalida" << endl;
    }
    else
    {
        cout << "Digite a sua senha: ";
        cin >> senhain;

        if (contaCliente->validaSenha(senhain))
        {
            cout << "Ola " << contaCliente->titular << endl;
            while (atendimento)
            {
                int op;
                double valor;
                cout << "Qual operacao deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Sair): ";
                cin >> op;
                switch (op)
                {
                case 1:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->saque(senhain,valor);
                    break;
                case 2:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->deposito(valor);
                    break;
                case 3:
                    cout << "Saldo: R$ "<<contaCliente->getSaldo(senhain)<<endl;
                    break;
                case 4:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    int numD;
                    cout << "Digite o número da conta de destino: ";
                    cin >> numD;
                    Conta *cdest;
                    cdest = this->buscaConta(numD);
                    contaCliente->transferencia(valor, senhain, cdest);
                    break;
                case 5:
                    atendimento = false;
                    break;
                }
            }
        }
        else
        {
            cout << "Senha invalida" << endl;
        }
    }
}

void Banco::atendimentoFuncionario(){
    int senhain;
    bool atendimento = true;
    cout << "Bem vindo ao sistema de atendimento do banco ao funcionário" << endl;
    cout << "Digite a sua senha: ";
    cin >> senhain;
    if (this->senhaFuncionario == senhain){
         cout << "Ola funcionário!" << endl;
            while (atendimento)
            {
                int opc;
                cout << "Qual operacao deseja fazer? (1 - Adicionar conta, 2 - Sair): ";
                cin >> opc;
                switch (opc)
                {
                    case 1:
                    {
                        int senha, numero;
                        std::string titular, tipo;
                        double saldo;
                        cout << "Digite a senha da conta a ser criada: ";
                        cin >> senha;
                        cout << "Digite o número da conta: ";
                        cin >> numero;
                        cout << "Digite o nome do titular: ";
                        cin >> titular;
                        cout << "Digite o tipo da conta (poupança/corrente): ";
                        cin >> tipo;
                        cout << "Digite a quantidade de dinheiro a ser depositada inicialmente na conta: ";
                        cin >> saldo;
                        adicionaConta(senha, numero, titular, tipo, saldo);
                        break;
                    }
                    case 2:
                        atendimento = false;
                        break;
                }
            }
    }
    else{
        cout << "Senha invalida" << endl;
    }
}

bool Banco::adicionaConta(int senha, int numero, std::string titular, std::string tipo, double saldo){
    if (this->quantidade < NUMCONTAS){
        Conta *novaConta = new Conta(senha, numero, titular, tipo, saldo);
        this->contas[this->quantidade] = *novaConta;
        this->quantidade++;
        return true;
    }
    else{
        cout << "Número de contas máximo atingido" << endl;
    }
    return false;
}
