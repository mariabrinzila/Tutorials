#include <iostream>

using namespace std;

//alg lui Euclid

int main()
{int a, b, r, i, n;
 cin>>n>>a;
 i=1;
 while (i<n)
       {cin>>b; //citim o noua valoare
        //calculam cmmdc dintre a si b
        while (b)
              {r=a%b;
               a=b;
               b=r;
              }
        i++;
       }
 cout<<a<<'\n';
 return 0;
}
