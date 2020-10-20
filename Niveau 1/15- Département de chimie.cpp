#include <bits/stdc++.h>

using namespace std;

int main(){
int nbPrise,minn,maxx,t;
cin>>nbPrise>>minn>>maxx;
bool alert = false;
while (nbPrise-- && !alert)
{
    cin>>t;
    if (t<minn || t>maxx)
    {
        cout<<"Alerte !!";
        alert = true;
    }
    else
        cout<<"Rien à signaler"<<endl;
}
return 0 ;
}
