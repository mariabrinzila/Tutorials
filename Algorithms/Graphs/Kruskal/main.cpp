#include <fstream>
#define MMAX 5005
#define NMAX 105

using namespace std;

ifstream fin("kruskal.in");
ofstream fout("kruskal.out");

struct muchie
      {
       int x, y, c;
      };

int n, m;
muchie L[MMAX];
int c[NMAX]; //c[i] este componeneta conexa din care face parte vf i
int a[NMAX]; //retinem indicii muchiilor selectate

void citire();
void sortare();
void kruskal();
void afisare();

int main()
{citire();
 sortare();
 kruskal();
 afisare();
 return 0;
 fin.close();
 fout.close();
}


void citire()
    {int i;
     fin>>n>>m;
     for (i=0; i<m; i++)
          fin>>L[i].x>>L[i].y>>L[i].c;
    }


void sortare()
    {int sch=1, i;
     muchie aux;
     do
       {sch=0;
        for (i=0; i<m-1; i++)
             if (L[i].c>L[i+1].c)
                 {aux=L[i]; L[i]=L[i+1];
                  L[i+1]=aux; sch=1;
                 }
       }
     while (sch);
    }


void kruskal()
    {int i, nr=0, j, mic, mare;
     for (i=1; i<=n; i++)
          c[i]=i;
     for (i=0; nr<n-1; i++)
          //analizam muchia i
          if (c[L[i].x]!=c[L[i].y])
              {//selectam muchia i
               a[nr++]=i;
               //unificam componenetele conexe ale extremitatilor acestei muchii
               mic=c[L[i].x]; mare=c[L[i].y];
               if (mic>mare)
                   {mic=c[L[i].y];
                    mare=c[L[i].x];
                   }
               for (j=1; j<=n; j++)
                    if (c[j]==mare)
                        c[j]=mic;
              }
    }


void afisare()
    {int i, cost=0;
     for (i=0; i<n-1; i++)
          cost+=L[a[i]].c;
     fout<<cost<<'\n';
     for (i=0; i<n-1; i++)
          fout<<L[a[i]].x<<' '<<L[a[i]].y<<'\n';
    }
