#include <fstream>
#define NMAX 100

using namespace std;

int n, m;
bool A[NMAX][NMAX];
int L[NMAX][NMAX];

void citire_matrice();
void citire_liste();
void afisare_matrice();
void afisare_liste();

int main()
{
 return 0;
}


void citire_matrice()
    {ifstream fin("graf.in");
     int i, x, y;
     fin>>n>>m;
     for (i=0; i<m; i++)
          {fin>>x>>y;
           A[x][y]=1;
          }
     fin.close();
    }


void citire_liste()
    {ifstream fin("graf.in");
     int i, x, y;
     fin>>n>>m;
     for (i=0; i<m; i++)
          {fin>>x>>y;
           L[x][0]++;
           L[x][L[x][0]]=y; //il adaug pe y la lista de adiacenta a lui x
          }
     fin.close();
    }


void afisare_matrice()
    {ofstream fout("graf.out");
     int i, j;
     for (i=0; i<n; i++)
          {for (j=0; j<n; j++)
                fout<<A[i][j]<<' ';
           fout<<'\n';
          }
     fout.close();
    }


void afisare_liste()
    {ofstream fout("graf.out");
     int i, j;
     for (i=0; i<m; i++)
          {for (j=1; j<=L[i][0]; i++)
                fout<<L[i][j];
           fout<<'\n';
          }
     fout.close();
    }
