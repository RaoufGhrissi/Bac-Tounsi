#include "robot.h"
using namespace std;
int main()
{
for (int i=1 ; i<11 ; i++)
{
   for (int j=0; j<i ; j++)
   droite();
   ramasser();
   for (int j=0; j<i ; j++)
   gauche();
   deposer();
}
return 0 ;}
