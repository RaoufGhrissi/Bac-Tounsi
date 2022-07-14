#include <iostream>

using namespace std;

char mat[1000][1000] ;
void carre(int d, int f, char c)
{   for (int i=d ; i<f+1 ; i++)
{
   for (int j=d ; j<f+1 ; j++) 
   {
      if (i==d || i==f ) mat[i][j] = c;
      else if ( j==d || j==f ) mat[i][j] = c;
   }
}

}


int main()
{
   int n;
   cin>>n;
   int i=0 , j=2*n-1 ;
   for (char c=97 ; c<98+n ; c ++ )
   {
         carre(i, j-1 , c) ;
         i++;
         j--;
   }
   
for (int i=0 ; i<2*n-1 ; i++)
{
   for (int j=0 ; j<2*n-1 ; j++) 
   {
      cout<<mat[i][j];
   }
   cout<<endl;
}
   
   
}