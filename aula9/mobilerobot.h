#ifndef MOBILEROBOT_H
#define MOBILEROBOT_H

#include <iostream>

using namespace std;

class MobileRobot
{
public:
    MobileRobot();
    MobileRobot(double X, double Y, double Z);
    ~MobileRobot();
    double getPosicaoAtual (char coordenada);
    virtual void Mover (double Xvel, double Yvel, double Zvel, double tempo) = 0;
 protected:
    double PosicaoAtual[3];
    void setPosicaoAtual (double X, double Y, double Z);
};

class RoboTerrestre:public MobileRobot
{
public:
    RoboTerrestre();
    RoboTerrestre(double X, double Y, double Z);
    ~RoboTerrestre();
    void Mover (double Xvel, double Yvel, double Zvel, double tempo);
};

class Quadrotor:public MobileRobot
{
public:
    Quadrotor();
    Quadrotor(double X, double Y, double Z);
    ~Quadrotor();
    void Mover (double Xvel, double Yvel, double Zvel, double tempo);
};

#endif
