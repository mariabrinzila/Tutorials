#include <iostream>

using namespace std;

int main()
{int n, d;
 cin>>n;
 cout<<1<<' ';
 d=2;
 while (d<=n)
       {if (n%d==0)
            cout<<d<<' ';
        d++;
       }
 return 0;
}
