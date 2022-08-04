#include <fstream>
#define NMAX 100

using namespace std;

ofstream fout("graf.out");

int n, m;
bool uz[NMAX];
bool A[NMAX][NMAX];
int L[NMAX][NMAX];

void citire_matrice();
void citire_liste();
void dfs_matrice(int x);
void dfs_liste(int x);

int main()
{int start=3;
 citire_matrice();
 dfs_matrice(start);
 fout.close();
 return 0;
}


void citire_matrice()
    {ifstream fin("graf.in");
     int i, x, y;
     fin>>n>>m;
     for (i=0; i<m; i++)
          {fin>>x>>y;
           A[x][y]=A[y][x]=1;
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
           L[y][0]++;
           L[y][L[y][0]]=x; //il adaug pe x la lista de adiacenta a lui y
          }
     fin.close();
    }


void dfs_matrice(int x)
    {int i;
     uz[x]=1; fout<<x<<' ';
     for (i=0; i<n; i++)
          if (A[x][i]==1 && uz[i]==0)
              dfs_matrice(i);
    }


void dfs_liste(int x)
    {int i;
     uz[x]=1; fout<<x<<' ';
     for (i=1; i<=L[x][0]; i++)
          if (uz[L[x][i]]==0)
              dfs_liste(L[x][i]);
    }
