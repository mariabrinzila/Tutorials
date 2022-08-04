#include <fstream>
#define NMAX 1000
#define INF 1000000000

using namespace std;

ifstream fin("graf.in");
ofstream fout("graf.out");

int n, m;
int cmin[NMAX][NMAX];

void citire();
void rf();
void afisare();

int main()
{citire();
 rf();
 afisare();
 return 0;
}


void citire()
    {int i, j, y, x, c;
     fin>>n>>m;
     for (i=1; i<=n; i++)
          {for (j=1; j<=n; j++)
                cmin[i][j]=INF;
           cmin[i][i]=0;
          }
     for (i=1; i<=m; i++)
          {fin>>x>>y>>c;
           cmin[x][y]=c;
          }
    }


void rf()
    {int z, x, y;
     for (z=1; z<=n; z++)
          for (x=1; x<=n; x++)
               for (y=1; y<=n; y++)
                    if (cmin[x][y]>cmin[x][z]+cmin[z][y])
                        {
                         cmin[x][y]=cmin[x][z]+cmin[z][y];
                        }
    }


void afisare()
    {int i, j;
     for (i=1; i<=n; i++)
          {for (j=1; j<=n; j++)
                fout<<cmin[i][j]<<' ';
           fout<<'\n';
          }
    }
