#include <bits/stdc++.h>

using namespace std;

int main(){
int nbMarchants;
cin>>nbMarchants;
int soumBaye3a[nbMarchants];
for (int indice=0 ; indice<nbMarchants ; indice++)
    cin>>soumBaye3a[indice];

int minimun = soumBaye3a[0];
int indiceBaye3 = 1;

for (int indice=1 ; indice<nbMarchants ; indice++)
{
    if (soumBaye3a[indice]<=minimun)
    {
        minimun = soumBaye3a[indice];
        indiceBaye3 = indice + 1;
    }
}

cout<<indiceBaye3;
return 0 ;
}
