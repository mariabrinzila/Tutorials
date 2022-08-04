#include <fstream>
#define NMAX 100

using namespace std;

ofstream fout("graf.out");

int n, m, prim, ultim;
bool viz[NMAX], C[NMAX];
int L[NMAX][NMAX];

void citire();
void bfs(int start);

int main()
{int start=3;
 citire();
 bfs(start);
 fout.close();
 return 0;
}


void citire()
    {ifstream fin("graf.in");
     int i, x, y;
     fin>>n>>m;
     for (i=0; i<m; i++)
          {fin>>x>>y;
           L[x][0]++;
           L[x][L[x][0]]=y; //il adaug pe y la lista de adiacenta a lui x
           L[y][0]++;
           L[y][L[y][0]]=x; //il adaug pe x la lista de adiacenta a lui y
          }
     fin.close();
    }


void bfs(int start)
    {int i, x;
     C[0]=start; prim=ultim=0;
     fout<<start<<' '; viz[start]=1;
     while (prim<=ultim) //coada nu e vida
            {x=C[prim]; prim++;
             //parcurgem vecinii lui x
             for (i=1; i<=L[x][0]; i++)
                  if (!viz[L[x][i]])
                      {viz[L[x][i]]=1; ultim++;
                       C[ultim]=L[x][i];
                       fout<<L[x][i]<<' ';
                      }
            }
    }
