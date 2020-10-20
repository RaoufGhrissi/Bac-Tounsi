#include <bits/stdc++.h>

using namespace std;


int main(){
int maPosition, nbVillage, positionVillage, nbVillageResultat = 0;
cin>>maPosition>>nbVillage;

for (int i=0 ; i<nbVillage ; i++)
{
    cin>>positionVillage;
    if (abs(maPosition - positionVillage)<=50)
        nbVillageResultat = nbVillageResultat + 1;
}

cout<<nbVillageResultat ;


return 0 ;
}
