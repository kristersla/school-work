//Dots naturāls skaitis n. Atrast visus tādu naturālu skaitļu trijniekus a, b, c , a <= b <= c <= n, lai a^2+b^2=c^2. Risinājumā izmantot funkciju, kas par trīs skaitļiem noskaidro, vai tie atbilst nosacījumam.


#include <iostream>

//Tiek pieveinota cmath biblioteka ar ko var veikt dažādas sarežģītas matemātikas darbības.

#include <cmath>

using namespace std;

//Tik uztaisīta galvanā int main funkcija, kur notiks visas darbības.

int main()
{
	int n; //Tiek deklarēts mainīs, tas būs lietotāja ievadītais skaitlis.

	cout<<"ievadi naturalu skaitli: ";
	cin>>n; //Ievada skaitli.

	//Tiek izveidots for loops, kur tiek padots jauns mainīagis c, kurš tiek pielīdzināts 1, lai sāk no 1, jo 0 nav naturāls skaitlis, tad for loops iet līdz c paliek lielāks vai vienāds ar n (lietotāja ievadīto skaitli), tad pie c katrā ciklā tiek pievienots + 1.

	for(int c=1; c<=n; c++)
		{

		//Tiek atkal izveidots for loops, kur tiek padots jauns mainīagis b, kurš tiek pielīdzināts 1, lai sāk no 1, jo 0 nav naturāls skaitlis, tad for loops iet līdz b paliek lielāks vai vienāds ar c, tad pie b katrā ciklā tiek pievienots + 1.

			for(int b=1; b<=c; b++)

			{

				//Tiek atkal izveidots for loops, kur tiek padots jauns mainīagis a, kurš tiek pielīdzināts 1, lai sāk no 1, jo 0 nav naturāls skaitlis, tad for loops iet līdz a paliek lielāks vai vienāds ar b, tad pie a katrā ciklā tiek pievienots + 1.

				for(int a=1; a<=b; a++)

				{
					//Tad tiek izveidots if funkcija, kas pasaka, ja c^2 ir vienāds ar a^2 + b^2, tad izprinēt a, b, c.

					if(pow(c,2) == pow(a,2) + pow(b,2))

					//Tiek izdrukātas vērtības a, b, c.

						cout<<a<<"^2 + "<<b<<"^2 = "<<c<<"^2"<<endl;

				}

			}

		}

}

//console:
//ievadi naturalu skaitli: 10
//3^2 + 4^2 = 5^2
//6^2 + 8^2 = 10^2
