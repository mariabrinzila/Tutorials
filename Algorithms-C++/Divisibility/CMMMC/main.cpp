#include <iostream>

using namespace std;

int main()
{int a, b, r, i, n, cmmmc, copie1, copie2;
 cin>>n>>a;
 i=1; cmmmc=0; copie1=a;
 while (i<n)
       {cin>>b; //citim o noua valoare
        copie2=b;
        //calculam cmmdc dintre a si b
        while (b)
              {r=a%b;
               a=b;
               b=r;
              }
        //calculam cmmmc si trecem la urmatorul numar
        cmmmc=(copie1*copie2)/a; i++; copie1=copie2;
       }
 cout<<cmmmc<<'\n';
 return 0;
}
