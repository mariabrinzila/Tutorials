#include <iostream>

using namespace std;

int n;
char sol[100];

void gen(int k);

int main()
{cin>>n;
 gen(1);
 return 0;
}


void gen(int k)
    {if (k-1==n)
         cout<<sol+1<<'\n';
         else
         {sol[k]='.'; gen(k+1);
          sol[k]='-'; gen(k+1);
         }
    }
