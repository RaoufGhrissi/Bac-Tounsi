#include <bits/stdc++.h>

using namespace std;

int os(string s, int p, char e)
{   
    int occ=0;
    for (int i=p ; i<(int)s.size() ; i++)
    {
        if (s[i]==e) occ++;
        else return occ;
    }
    return occ;
}

int main()

{
   string s;
   cin>>s;
   int o=1;
   while (o)
   {   
   o=0;
   string c="";
   int i=0;
   while( i<(int)s.size() )
   { 
    char w=s[i];
    int a=os(s,i,w);
    if (a%2) { c+=s[i]; o++ ;i+=a ;}
    else i+=a ;
    if (s==c) o=0;
    if (i>=(int)s.size()) s=c;
    
   }
    
   }
   
   cout<<s;
}