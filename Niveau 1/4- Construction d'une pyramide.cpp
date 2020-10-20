#include <iostream>
using namespace std;
int main()
{
int somme = 0 ;
for (int i=1 ; i<18 ; i+=2)
{
somme=somme + i*i*i;
}
cout<<somme;

}