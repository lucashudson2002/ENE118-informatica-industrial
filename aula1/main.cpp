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
    cout << "Seu indice de massa corporal e: " << imc << endl;
    if (imc < 18.5)
        cout << "Voce esta abaixo do peso" << endl;
    else if (imc < 24.9)
        cout << "Voce esta com peso normal" << endl;
    else if (imc < 29.9)
        cout << "Voce esta acima do peso" << endl;
    else
        cout << "Voce esta obeso" << endl;
        
    return 0;
}

