#include <iostream>

using namespace std;

int main()
{
   int n;
   cin>>n;
   int p1=0,p2=0;
   while(n--)
   {
      int a,b;
      cin>>a>>b;
      p1+=a;
      p2+=b;      
   }

   if (p1>p2) cout<<"L'équipe 1 a un avantage"<<endl;
   else cout<<"L'équipe 2 a un avantage"<<endl;
   cout<<"Poids total pour l'équipe 1 : "<<p1<<endl;
   cout<<"Poids total pour l'équipe 2 : "<<p2;
}