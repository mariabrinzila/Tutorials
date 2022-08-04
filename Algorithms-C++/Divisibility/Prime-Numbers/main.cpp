#include <iostream>

using namespace std;

int main()
{int n, d, nrd;
 cin>>n;
 if (n==1)
     nrd=1;
     else
     {nrd=2; d=2;
      while (d*d<=n)
             {if (n%d==0)
                  {nrd++;
                   break;
                  }
              d++;
             }
     }
 if (nrd==2)
     cout<<"Este prim"<<'\n';
     else
     cout<<"Nu este prim"<<'\n';
 return 0;
}
