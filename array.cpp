#include <iostream>
using namespace std;

/*Uzrakstīt programmu, kas izveido masīvu ar 3 integer vērtībām (vērtības nosakat paši). Programmai vajag atrast lielāko un mazāko vērtību šajā masīvā8*/

int main()
{
   int x[3];

   cout<<"ievadi tris vertibas: \n";
   cin>>x[0]>>x[1]>>x[2];
   cout<<endl;

    if(x[0]>x[1] && x[0]>x[2]){

      cout<<"Lielakais ir "<<x[0];
      cout<<" un ";

    }else if(x[1]>x[0] && x[1]>x[2]){

      cout<<"Lielakais ir "<<x[1];
      cout<<" un ";

    }else if(x[2]>x[0] && x[2]>x[1]){

      cout<<"Lielakais ir "<<x[2];
      cout<<" un ";

    }


    if (x[0]<x[1] && x[0]<x[2]){

        cout<<"mazakais skaitlis ir "<<x[0];


    }else if(x[1]<x[0] && x[1]<x[2]){

        cout<<"mazakais skaitlis ir "<<x[1];

    }else if(x[2]<x[0] && x[2]<x[1]){

        cout<<"mazakais skaitlis ir "<<x[2];

    }






    return 0;
}
