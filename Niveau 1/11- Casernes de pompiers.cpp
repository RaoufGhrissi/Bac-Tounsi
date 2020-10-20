#include <bits/stdc++.h>

using namespace std;

int main(){
int nbComparaison;
cin>>nbComparaison;
int xd0,xf0,yd0,yf0;
int xd1,xf1,yd1,yf1;

for (int i=0 ; i<nbComparaison ; i++)
{
    cin>>xd0>>xf0>>yd0>>yf0>>xd1>>xf1>>yd1>>yf1;
    if (xd0>=xf1 || xd1>=xf0 || yd0>=yf1 || yd1>=yf0)
        cout<<"NON"<<endl;
    else
        cout<<"OUI"<<endl;
}
return 0 ;
}
