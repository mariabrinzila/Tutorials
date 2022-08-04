#include <iostream>

using namespace std;

int n, m;
int sol[100];

void gen(int k);
void afisare();

int main()
{cin>>n>>m;
 gen(1);
 return 0;
}


void gen(int k)
    {int i;
     if (k-1==m)
         afisare();
         else
         for (i=sol[k-1]+1; i<=n-m+k; i++)
              {sol[k]=i;
               gen(k+1);
              }
    }


void afisare()
    {int i;
     for (i=1; i<=m; i++)
          cout<<sol[i]<<' ';
     cout<<'\n';
    }
