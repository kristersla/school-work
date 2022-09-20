#include <iostream>
using namespace std;

int main(){

    int x, y, z;

    cout<<"Programma kura parbaudis vai tas ir trijsturis.\n";
    cout<<"ievadi 3 malu garumus:\n";
    cout<<endl;
    cin>>x>>y>>z;

    if (x+y>z && y+z>x && z+x>y){

        cout<<endl;
        cout<<"Eksiste";

    }else{
        cout<<endl;
        cout<<"Neeksiste";

    }

}
