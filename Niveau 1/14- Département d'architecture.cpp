#include <bits/stdc++.h>

using namespace std;

int main()
{
   int n;
   cin>>n;
   int s=0;

int i=1 ;   
while( s<=n )
   {  int prec = s;
      s = s + pow(i,2);
      if ( s>n ) { cout<<i-1<<endl<<prec; return 0; }
      else i++;
   }
}