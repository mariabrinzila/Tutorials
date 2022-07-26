#include <iostream>
#define NMAX 1001
#define INF 100000000

using namespace std;

struct varf
      {
       int vf, c;
      };

int n, m, start;
varf G[NMAX][NMAX];
int gr[NMAX]; //gr[i]=gradul/gradul exterior varfului i
bool M[NMAX];
int dmin[NMAX], prec[NMAX], drum[NMAX];

void citire();
void dijkstra();
void afisare();

int main()
{citire();
 dijkstra();
 afisare();
 return 0;
}


void citire()
    {int x, y, cost, i;
     cin>>n>>m>>start;
     for (i=0; i<m; i++)
          {cin>>x>>y>>cost;
           G[x][gr[x]].vf=y;
           G[x][gr[x]].c=cost;
           gr[x]++;
          }
     M[start]=1;
     for (i=1; i<=n; i++)
          {dmin[i]=INF;
           prec[i]=start;
          }
     prec[start]=0; dmin[start]=0;
     for (i=0; i<gr[start]; i++)
          dmin[G[start][i].vf]=G[start][i].c;
    }


void dijkstra()
    {int j, i, vfmin, cmin, x;
     for (j=0; j<n; j++)
          {//aflu vfmin
           cmin=INF+1;
           for (x=1; x<=n; x++)
                if (!M[x] && dmin[x]<cmin)
                    {cmin=dmin[x];
                     vfmin=x;
                    }
           if (cmin==INF)
               break;
           M[vfmin]=1;
           for (i=0; i<gr[vfmin]; i++)
                if (!M[G[vfmin][i].vf])
                    if (dmin[G[vfmin][i].vf]>dmin[vfmin]+G[vfmin][i].c)
                        {dmin[G[vfmin][i].vf]=dmin[vfmin]+G[vfmin][i].c;
                         prec[G[vfmin][i].vf]=vfmin;
                        }
          }
    }


void afisare()
    {int x, lg, i;
     for (x=1; x<=n; x++)
          if (dmin[x]==INF)
              cout<<"Nu exista drum de la "<<start<<" la "<<x<<'\n';
              else
              {cout<<"Costul drumului de cost minim de la "<<start<<" la "<<x<<" este "<<dmin[x]<<'\n';
               drum[0]=x; lg=1;
               while (drum[lg-1]!=start)
                      {drum[lg]=prec[drum[lg-1]];
                       lg++;
                      }
               for (i=lg-1; i>=0; i--)
                    cout<<drum[i]<<' ';
               cout<<'\n';
              }
    }
