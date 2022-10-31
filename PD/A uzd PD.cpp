
//A uzdevums pārbaudes darbā, kur lietotajs ievada divus veselus skaitlus vai ciparus un programma izdruka visus kopīgos dalītājus, tad programmaij ir jābūt iespējai veikt darbu vēlreiz.

#include <iostream>

using namespace std;

//Sākumā tiek izveidota funkcija void, jo neko nevajag atgriezt tikai pilda doto uzdevumu. Void funkcijā ir 3 mainīgie.

void dal(int x, int y){

	//Tiek izveidots for loop cikls tajā tiek pielīdzināts mainīgais i = 1, kas būs mūsu noteicējs vai turpinās cikls, ja i ir mazāks par x un y, tad pieskaitās pie i + 1 un notiek if funkcija.
	//if funkcija kurā dotie cipari/skaitļi tiek izdalīti, ja atlikums dalijumam ir 0, tad tiek izprinēets dalījums.

	for(int i = 1; i<=x&&y; ++i){

		if(x&&y % i == 0){

		cout<<i<<" ";
	}

 }

}

//Galvana main funkcija no kura tiek padoti mainigie void dal funkcijai.
int main()
{

//Tiek deklerēti mainīgie

    int x, y, i;

    char u = 'y';
    char tur = 'y';

	cout<<"Si ir programma kura paska kopigos dalitajus starp diviem veseliem skaitliem."<<endl;
	cout<<endl;
	cout<<endl;

//Tiek izveidota while funkcija, kas turpina programmu līdz to apstādina. While loop strādā - kamēr y ir vienāds ar y, tā darbosies, bet ja y būs vienāds ar ko citu tā beigs savu darbību.
    while(tur == u){

		cout<<"Ievadi pirmo veselo skaitli vai ciparu:"<<endl;
		cin>>x; //Tiek ievadīts pirmais cipars/skaitlis.
		cout<<"Ievadi otro veselo skaitli vai ciparu:"<<endl;
		cin>>y; //Tiek ievadīts otrais cipars/skaitlis.
		cout<<endl;
		cout<<"Visi kopigie dalitaji:"<<endl;

//Tiek padota void dal funkcijas rezultāts uz int main funckiju.

		dal(x,y);

		cout<<endl;
		cout<<endl;

//Tiek piedāvāts vai vēlaties turpināt šo programmu vēlreiz.

		cout<<"Velies meginat velreiz (y/n)"<<endl;
		cin>>tur; //Tiek ievadīta atbilde, ja atbilde ir y, tad programma tiek atkārtoti palaista, ja n, tad while loop izbeidzas.
		cout<<endl;



    }
//Kad while loop ir izbeigts, tad tiek izprinēts šis.

    cout<<"Paldies par darbu!"<<endl;
}
