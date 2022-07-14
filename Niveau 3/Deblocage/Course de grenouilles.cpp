#include <bits/stdc++.h>

using namespace std;

int main()
{
   int g,t;
   cin>>g>>t;
   int tab[g+1];
   int n[g+1];
   memset(tab,0,sizeof(tab));
   memset(n,0,sizeof(n));
    t--;
   while(t--)
   {
      int p,d;
      cin>>p>>d;
      tab[p]+=d;
      int m=0,occ=0;
      for (int i=1 ; i<g+1 ; i++)
         m=max(m,tab[i]);
      int a;
      for (int i=1 ; i<g+1 ; i++)
         if (m==tab[i]) { occ++; a=i; }
         
    if (occ==1) n[a]++;

       
   }
   
   int m=0;
    for (int i=1 ; i<g+1 ; i++)
         m=max(m,n[i]);
    for (int i=1 ; i<g+1 ; i++)
         if (m==n[i]) { cout<<i ; return 0 ; }
}