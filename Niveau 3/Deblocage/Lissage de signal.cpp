#include <iostream>

using namespace std;
double abss(double n)
{
   if (n>0) return n;
   else return -n ;
}

int main()
{
   int n;
   cin>>n;
   double d;
   cin>>d;
   double tab[n];
   double v[n];

   for (int i=0;i<n ;i++)
      cin>>tab[i];
   for (int i=0;i<n ;i++)
      v[i]=tab[i];
   bool b = false ;
         for (int i=0 ; i<n-1 ; i++)
      {
         if (abss(tab[i]-tab[i+1])>d) { b=true ; break ; }
      }   
   int c=0;
   while(b)
   {  c++;
      b=false;
      for (int i=1 ; i<n-1 ; i++)
      {
         v[i]=(tab[i-1]+tab[i+1])/2 ;
      }
      for (int i=0;i<n ;i++)
         tab[i]=v[i];
      for (int i=0 ; i<n-1 ; i++)
      {
         if (abss(tab[i]-tab[i+1])>d) { b=true ; break ; }
      }
      
   }
   cout<<c;
}