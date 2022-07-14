#include <bits/stdc++.h>
using namespace std;
int wa9techTnajemTetsalfou[1000];

int main(){
int nbLivres,nbJours;
cin>>nbLivres>>nbJours;
memset(wa9techTnajemTetsalfou, -1, sizeof(wa9techTnajemTetsalfou));

for (int jour = 1 ; jour<=nbJours ; jour++)
{
    int nbClients;
    cin>>nbClients;
    while(nbClients--)
    {
        int livre, duree;
        cin>>livre>>duree;
        if (wa9techTnajemTetsalfou[livre]<=jour)
        {
            cout<<1<<endl;
            wa9techTnajemTetsalfou[livre] = jour + duree;
        }
        else
            cout<<0<<endl;
    }
}

}
