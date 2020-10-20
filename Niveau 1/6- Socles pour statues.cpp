#include <bits/stdc++.h>

using namespace std;

int main(){
int fin,debut;
int somme = 0;
cin>>fin>>debut;

for (int i=debut ; i<=fin ; i++)
    somme = somme + ( i*i );

   cout<<somme;

return 0 ;
}
