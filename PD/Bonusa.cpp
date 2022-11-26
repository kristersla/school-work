#include <iostream>
#include <fstream> //Seit tiek pievienota biblioteka, lai atvertu failus uz datora
#include <bits/stdc++.h> //Seit tiek pievienota biblioteka, lai varetu saskaitit vienados burtus.

using namespace std;


//Šeit tiek izveidota funkcija "biez", kura izskaita cik reizes atkartojas viens burts un tad tos ieliek iekš faila F1.txt.

void biez(string output){

    int a=count(output.begin(),output.end(),'a'); //Šeit tiek izskaitīts cik reizes parādās 'a' burts tekstā.
    int b=count(output.begin(),output.end(),'b');
    int c=count(output.begin(),output.end(),'c');
    int d=count(output.begin(),output.end(),'d');
    int e=count(output.begin(),output.end(),'e');
    int f=count(output.begin(),output.end(),'f');
    int g=count(output.begin(),output.end(),'g');
    int h=count(output.begin(),output.end(),'h');
    int i=count(output.begin(),output.end(),'i');
    int j=count(output.begin(),output.end(),'j');
    int k=count(output.begin(),output.end(),'k');
    int l=count(output.begin(),output.end(),'l');
    int m=count(output.begin(),output.end(),'m');
    int n=count(output.begin(),output.end(),'n');
    int o=count(output.begin(),output.end(),'o');
    int p=count(output.begin(),output.end(),'p');
    int q=count(output.begin(),output.end(),'q');
    int r=count(output.begin(),output.end(),'r');
    int s=count(output.begin(),output.end(),'s');
    int t=count(output.begin(),output.end(),'t');
    int u=count(output.begin(),output.end(),'u');
    int v=count(output.begin(),output.end(),'v');
    int w=count(output.begin(),output.end(),'w');
    int x=count(output.begin(),output.end(),'x');
    int y=count(output.begin(),output.end(),'y');
    int z=count(output.begin(),output.end(),'z');


    //Tad tiek atvērts F1.txt fails un tiek ievadītas visas saskaitītās vērtības.

    ofstream myfile;
    myfile.open ("C:\\Users\\burka\\OneDrive\\Desktop\\bonus uzd\\F1.txt");
    myfile <<"A - "<<a<<"\n";
    myfile <<"B - "<<b<<"\n";
    myfile <<"C - "<<c<<"\n";
    myfile <<"D - "<<d<<"\n";
    myfile <<"E - "<<e<<"\n";
    myfile <<"F - "<<f<<"\n";
    myfile <<"G - "<<g<<"\n";
    myfile <<"H - "<<h<<"\n";
    myfile <<"I - "<<i<<"\n";
    myfile <<"J - "<<j<<"\n";
    myfile <<"K - "<<k<<"\n";
    myfile <<"L - "<<l<<"\n";
    myfile <<"M - "<<m<<"\n";
    myfile <<"N - "<<n<<"\n";
    myfile <<"O - "<<o<<"\n";
    myfile <<"P - "<<p<<"\n";
    myfile <<"Q - "<<q<<"\n";
    myfile <<"R - "<<r<<"\n";
    myfile <<"S - "<<s<<"\n";
    myfile <<"T - "<<t<<"\n";
    myfile <<"U - "<<u<<"\n";
    myfile <<"V - "<<v<<"\n";
    myfile <<"W - "<<w<<"\n";
    myfile <<"X - "<<x<<"\n";
    myfile <<"Y - "<<y<<"\n";
    myfile <<"Z - "<<z;

    myfile.close(); //Šeit failu F1.txt aizver.


}

//Šeit tiek izveidota galvenā funkcija.

int main () {


 ifstream read;
 read.open("C:\\Users\\burka\\OneDrive\\Desktop\\bonus uzd\\F.txt"); //Tiek atvērts fails F.txt, kurā ir string ar tekstu un tas tiek nolasiīts.
 char output[100];
 if (read.is_open()){//Tad to nolasa un padod tālāk funkcijām.

    while (!read.eof()){


        read >> output;



 }
}
    cout<<"Ir! apskaties file ar nosaukumu: F1.txt"<<endl;

    //Tiek izpildītās funckijas
    read.close();
    biez(output);

}
