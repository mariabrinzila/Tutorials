#include <iostream>
#define NMAX 100

using namespace std;

/*ifstream fin("graf.in");
ofstream fout("graf.out");*/

int n, m, nrc, poz;
int G[NMAX][NMAX], GT[NMAX][NMAX];
int viz[NMAX], postord[NMAX];

void citire();
void dfs(int x);
void dfst(int x);

int main()
{int i;
 citire();
 for (i=1; i<=n; i++)
      if (!viz[i])
          dfs(i);
 for (i=n; i>0; i--)
      if (viz[postord[i]])
          {cout<<"Componeneta "<<++nrc<<": ";
           dfst(postord[i]);
           cout<<'\n';
          }
 return 0;
}


void citire()
    {int i, x, y;
     cin>>n>>m;
     for (i=1; i<=m; i++)
          {cin>>x>>y;
           G[x][0]++; G[x][G[x][0]]=y;
           GT[y][0]++; GT[y][GT[y][0]]=x;
          }
    }


void dfs(int x)
    {int i;
     viz[x]=1;
     for (i=1; i<=G[x][0]; i++)
          if (!viz[G[x][i]])
              dfs(G[x][i]);
     postord[++poz]=x;
    }


void dfst(int x)
    {int i;
     viz[x]=0; cout<<x<<' ';
     for (i=1; i<=GT[x][0]; i++)
          if (viz[GT[x][i]])
              dfst(GT[x][i]);
    }
