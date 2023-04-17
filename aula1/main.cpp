#include <iostream>

using namespace std;

int main()
{
    
    float peso, altura, imc;
    cout << "Digite seu pego em kg: ";
    cin >> peso;
    cout << "Digite sua altura em metros: ";
    cin >> altura;
    imc = peso/altura/altura;
    cout << "Seu índice de massa corporal é: " << imc << endl;
    if (imc < 18.5)
        cout << "Você está abaixo do peso" << endl;
    else if (imc < 24.9)
        cout << "Você está com peso normal" << endl;
    else if (imc < 29.9)
        cout << "Você está acima do peso" << endl;
    else
        cout << "Você está obeso" << endl;
        
    return 0;
}

