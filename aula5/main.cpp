#include <iostream>
#include "banco.h"
using namespace std;

int main()
{
    Banco b1;
    int opc;
    cout << "Olá! Você é:" << endl;
    cout << "1) Cliente" << endl;
    cout << "2) Funcionário" << endl;
    cout << "Opção: ";
    cin >> opc;
    while (opc<1 || opc>2){
        cout << "Opção inválida, tente outra: ";
        cin >> opc;
    }
    switch(opc){
        case 1:
            b1.atendimentoCliente();
            break;
        case 2:
            b1.atendimentoFuncionario();
            break;
    }

    return 0;
}