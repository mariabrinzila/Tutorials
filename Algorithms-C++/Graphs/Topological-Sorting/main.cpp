#include <fstream>
#define NMAX 1000

using namespace std;

ifstream fin("graf.in");
ofstream fout("graf.out");

int G[NMAX][NMAX], gi[NMAX], niv[NMAX];
int n, m, nr;

void citire();
void niveluri();

int main()
{citire();
 niveluri();
 return 0;
 fin.close();
 fout.close();
}


void citire()
    {int i, x, y;
     fin>>n>>m;
     for (i=1; i<=m; i++)
          {fin>>x>>y;
           G[x][0]++;
           G[x][G[x][0]]=y;
           gi[y]++;
          }
    }


void niveluri()
    {int i, j, lg;
     while (nr<n)
            {lg=0;
             for (i=1; i<=n; i++)
                  if (gi[i]==0)
                      niv[++lg]=i;
             for (i=1; i<=lg; i++)
                  {fout<<niv[i]<<' ';
                   gi[niv[i]]=-1; nr++;
                   for (j=0; j<G[niv[i]][0]; j++)
                        gi[G[niv[i]][j]]--;
                  }
            }
    }
