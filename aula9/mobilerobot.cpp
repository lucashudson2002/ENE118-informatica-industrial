#include "mobilerobot.h"

MobileRobot::MobileRobot() : MobileRobot(0,0,0)
{}

MobileRobot::MobileRobot(double X, double Y, double Z)
{
    setPosicaoAtual(X, Y, Z);
}

MobileRobot::~MobileRobot()
{}

double MobileRobot::getPosicaoAtual (char coordenada)
{
    switch(coordenada){
        case 'x': case'X':
            return PosicaoAtual[0];
            break;
        case 'y': case'Y':
            return PosicaoAtual[1];
            break;
        case 'z': case'Z':
            return PosicaoAtual[2];
            break;
        default:
            cout << "Erro ao pegar a coordenada " << coordenada << endl;
            return 0;
    }
}

void MobileRobot::setPosicaoAtual (double X, double Y, double Z)
{
    PosicaoAtual[0] = X;
    PosicaoAtual[1] = Y;
    PosicaoAtual[2] = Z;
}

RoboTerrestre::RoboTerrestre() : MobileRobot()
{}

RoboTerrestre::RoboTerrestre(double X, double Y, double Z) : MobileRobot(X, Y, 0)
{}

RoboTerrestre::~RoboTerrestre()
{}

void RoboTerrestre::Mover (double Xvel, double Yvel, double Zvel, double tempo)
{
    cout << "Acionando os motores das rodas.." << endl;
    cout << "Posição antes do movimento:" << endl;
    cout << "X = " << PosicaoAtual[0] << endl;
    cout << "Y = " << PosicaoAtual[1] << endl;
    cout << "Z = " << PosicaoAtual[2] << endl;
    PosicaoAtual[0] += Xvel * tempo;
    PosicaoAtual[1] += Yvel * tempo;
    PosicaoAtual[2] = 0;
    cout << "Posição depois do movimento:" << endl;
    cout << "X = " << PosicaoAtual[0] << endl;
    cout << "Y = " << PosicaoAtual[1] << endl;
    cout << "Z = " << PosicaoAtual[2] << endl;
}

Quadrotor::Quadrotor() : MobileRobot()
{}

Quadrotor::Quadrotor(double X, double Y, double Z) : MobileRobot(X, Y, Z)
{}

Quadrotor::~Quadrotor()
{}

void Quadrotor::Mover (double Xvel, double Yvel, double Zvel, double tempo)
{
    cout << "Acionando hélices..." << endl;
    cout << "Posição antes do movimento:" << endl;
    cout << "X = " << PosicaoAtual[0] << endl;
    cout << "Y = " << PosicaoAtual[1] << endl;
    cout << "Z = " << PosicaoAtual[2] << endl;
    PosicaoAtual[0] += Xvel * tempo;
    PosicaoAtual[1] += Yvel * tempo;
    PosicaoAtual[2] += Zvel * tempo;
    cout << "Posição depois do movimento:" << endl;
    cout << "X = " << PosicaoAtual[0] << endl;
    cout << "Y = " << PosicaoAtual[1] << endl;
    cout << "Z = " << PosicaoAtual[2] << endl;
}