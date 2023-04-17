#include "robot.h"

int main()
{
    Robot vsss = {"Vsss", 0, 0, 10, 5};
    Robot seguidor = {"Ratão", 0, 0, 1, 1};
    vsss.showPos();
    vsss.move(2);
    vsss.showPos();
    vsss.changeSpeed(2,3);
    vsss.move(5);
    vsss.showPos();
    return 0;
}