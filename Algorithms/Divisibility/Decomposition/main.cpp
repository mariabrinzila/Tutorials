#include <iostream>

using namespace std;

int main()
{int n, m, d;
 cin>>n;
 d=2;
 while (n>1) //n mai are divizori
       {m=0;
        while (n%d==0)
              {n=n/d;
               m++;
              }
        if (m)
            cout<<d<<' '<<m<<'\n';
        d++;
       }
 return 0;
}
