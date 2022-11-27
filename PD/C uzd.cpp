//Dots divu dimensiju masīvs A(n,n), kas aizpildīts ar nullēm un vieniniekiem (masīvu izveidot un ieraksīt tajā vērtības pašiem).
//Noskaidrot, cik masīva kolonnu un rindu ir aizpildītas tikai ar 1 un cik kolonnu un rindu ir aizpildītas tikai ar 0.
//Izveidot un izmantot funkciju vai funkcijas, kas vienai rindai vai kolonnai var pateikt, ka tā sastāv tikai no 1 vai 0.

#include <iostream>
using namespace std;

//Sākumā tiek izveidota funkcija void, jo neko nevajag atgriezt tikai pilda doto uzdevumu.
//Funkcija iziet cauri katrai vērtībai katrā rindā, tad ja vērtība ir 0 vai 1 to pieskaita pie attiecigajaiem mainigajiem.

//Šaja gadijuma viena rinda ir 5 vertibas, tapec ja mainigais ir 5, tad visa rinda ir tikai vieninieki un tas pats atkartojas ar nullem.
void row(int masivs[4][5]){ //Sākumā tiek pievienots massivs kuram ir 4 kollonas ar 5 rindam.
    int null, one; //tiek definetas nulles un vieninieki.

    for(int i=0; i<4; i++){ //Kamer i ir mazāks par 4 for loop strādā un pēc katra cikla i tiek pieskaitīts viens.

    //sakuma vertiba vieniniekam & nullej tiek pieskirta 0.
        one = 0;

        null = 0;

        for(int n = 0; n<5; n++){ //Kamer n ir mazāks par 5 for loop strādā un pēc katra cikla n tiek pieskaitīts viens.

            int k = masivs[i][n]; //k ir masīvs ar jaunajām i & n vērtībām.

            if(k == 1){

                one++; //ja k vērtība ir 1, tad pieskaita klāt vienu.

            }else if(k == 0){

                null++; //ja k vērtība ir 0, tad pieskaita klāt vienu.

            }
            if(one == 5){ //Ja visa rina ir ar vininiekiem, tad izprintē - Rinda ar 1 un kura rindā atrodas.

                cout<<"Rinda ar 1 "<<i+1<<" rinda"<<endl;

            }
            else if(null == 5){ //Ja visa rina ir ar nullēm, tad izprintē - Rinda ar 0 un kura rindā atrodas.

                cout<<"Rinda ar 0 "<<"atrodas "<<i+1<<" rinda"<<endl;
            }
        }
    }
}


//Seit ir redzama līdzīga funkcija pirmajai, bet šeit tiek nolasīta katra vērtība no kollonas. Tas pats attkartojas tikai mainās vērtības pie for cikliem, jo tās ir attiecīgas kollonām.
void column(int masivs[4][5]){
    int null, one;
    for(int i=0; i<5; i++){

        one = 0;

        null = 0;

        for(int n=0; n<4; n++){

            int k = masivs[n][i];
            if(k == 1){

                one++;

            }else if(k == 0){

                null++;

            }

            if(one == 4){

                cout<<"Kollona ar l "<<i+1<<" kollona"<<endl;

            }
            else if(null == 4){

                cout<<"Kollona ar 0 "<<"atrodas "<<i+1<<" kollona"<<endl;

            }
        }
    }
}


//Seit ir galvana funkcija kur ir deklarēts massīvs ar visām vertibam un tiek palaistas abas funkcijas.
int main()
{

    int masivs[4][5] = {{0, 0, 0, 0, 0}, {1, 0, 0, 0, 0}, {0,1,0,1,0}, {1,1,1,1,0}};

    row(masivs);
    column(masivs);

}


//console: 
//Rina ar 0 atrodas 1 rinda
//Kollona ar 0 atrodas 5 kollona
