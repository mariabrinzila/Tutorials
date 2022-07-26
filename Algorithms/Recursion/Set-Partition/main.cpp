#include <iostream>

using namespace std;

int p[100];
int n, nrs;

void gen(int k);
void afisare();

int main()
{cin>>n;
 gen(1);
 return 0;
}


void gen(int k)
    {int i, j;
     if (k==n+1)
         afisare();
         else
         {//ori punem elementul k succesiv intr-una dintre submultimile deja existente
          for (i=1; i<=nrs; i++)
              {p[k]=i;
               gen(k+1);
              }
          //ori facem o submultime noua doar cu k
          nrs++; p[k]=nrs;
          gen(k+1);
          nrs--;
         }
    }


void afisare()
    {int i, j;
     for (i=1; i<=nrs; i++)
          {cout<<'{'<<' ';
           for (j=1; j<=n; j++)
                if (p[j]==i) //daca elementul j este in submultimea i
                    cout<<j<<' ';
           cout<<'}'<<' ';
          }
     cout<<'\n';
    }
