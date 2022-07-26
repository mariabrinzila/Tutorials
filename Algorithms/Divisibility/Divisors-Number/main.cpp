#include <iostream>

using namespace std;

int main()
{int n, d, nrd;
 cin>>n;
 if (n==1)
     nrd=1;
 nrd=1; d=2;
 while (d<=n)
       {if (n%d==0)
            nrd++;
        d++;
       }
 cout<<nrd<<'\n';
 return 0;
}
