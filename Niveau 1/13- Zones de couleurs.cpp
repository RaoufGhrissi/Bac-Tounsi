#include <iostream>

using namespace std;
int main()
{
   int n;
   cin>>n;
   while ( n-- )
   {
      int x,y;
      cin>>x>>y;
      
      if ( x<0 || x>90 || y<0 || y>70 ) 
         cout<<"En dehors de la feuille"<<endl; 
      else if  ( ( (x>10 && x<85) && (( y>10 && y<20 )  || ( y>45 && y<55 ) ) ) || 
      ( ( (x>10 && x<25) || ( x>50 && x<85 )) && ( y>20 && y<45 ) ) ) 
         cout<<"Dans une zone bleue"<<endl; 
      else if (((x>15 && x<45 ) || ( x>60 && x<85 ) ) && ( y>60 && y<70 ) )
         cout<<"Dans une zone rouge"<<endl; 
      else 
         cout<<"Dans une zone jaune"<<endl; 
}
}