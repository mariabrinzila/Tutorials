#include <fstream>
#define NMAX 105
#define INFINIT 1000000000

using namespace std;

ifstream fin("prim.in");
ofstream fout("prim.out");

struct muchie
      {
       int y, c;
      };

muchie G[NMAX][NMAX];
int d[NMAX]; //d[x]=gradul lui x
int n, m, start=1;
bool S[NMAX];
int cmin[NMAX], vfmin[NMAX];

void citire();
void initializare();
void prim();
void afisare();

int main()
{citire();
 initializare();
 prim();
 afisare();
 return 0;
 fin.close();
 fout.close();
}


void citire()
    {int i, x, y, cost;
     fin>>n>>m;
     for (i=0; i<m; i++)
          {fin>>x>>y>>cost;
           d[x]++;
           G[x][d[x]].y=y; G[x][d[x]].c=cost;
           d[y]++;
           G[y][d[y]].y=x; G[y][d[y]].c=cost;
          }
    }


void initializare()
    {int i;
     S[start]=1;
     for (i=1; i<=n; i++)
          {cmin[i]=INFINIT;
           vfmin[i]=start;
          }
     vfmin[start]=0; cmin[start]=0;
     for (i=1; i<=d[start]; i++)
          cmin[G[start][i].y]=G[start][i].c;
    }


void prim()
    {int i, minim, vf, j;
     for (i=1; i<n; i++)
          {//determin un vf neselectat de cost minim
           minim=INFINIT;
           for (j=1; j<=n; j++)
                if (!S[j] && cmin[j]<minim)
                    {minim=cmin[j];
                     vf=j;
                    }
           //selectez vf
           S[vf]=1;
           //actualizez eventual costurile catre celelalte varfuri neselectate
           for (j=1; j<=d[vf]; j++)
                if (!S[G[vf][j].y] && cmin[G[vf][j].y]>G[vf][j].c)
                    {cmin[G[vf][j].y]=G[vf][j].c;
                     vfmin[G[vf][j].y]=vf;
                    }
          }
    }


void afisare()
    {int i, costapm=0;
     for (i=1; i<=n; i++)
          costapm+=cmin[i];
     fout<<costapm<<'\n';
     for (i=1; i<=n; i++)
          fout<<vfmin[i]<<' ';
     fout<<'\n';
    }
