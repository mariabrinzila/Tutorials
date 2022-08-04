#include <iostream>

using namespace std;

int n;
int sol[100];
bool uz[100];

void gen(int k);
void afisare();

int main()
{cin>>n;
 gen(1);
 return 0;
}


void gen(int k)
    {int i;
     if (k-1==n)
         afisare();
         else
         for (i=1; i<=n; i++)
              if (uz[i]==0)
                  {sol[k]=i; uz[i]=1;
                   gen(k+1); uz[i]=0;
                  }
    }


void afisare()
    {int i;
     for (i=1; i<=n; i++)
          cout<<sol[i]<<' ';
     cout<<'\n';
    }
