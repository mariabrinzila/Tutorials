#include <iostream>

#define NMAX 100

using namespace std;

int n, m, k;
bool uz[NMAX];
bool A[NMAX][NMAX];

void citire_matrice();
void dfs_matrice(int x);
void descompunere();

int main()
{
    citire_matrice();
    descompunere();
    return 0;
}


void citire_matrice()
{
    int i, x, y;
    //citim nr de varfuri si nr de muchii si nr de varfuri din partitie
    cin >> n >> m >> k;
    for (i = 0; i < m; i++)
    {
        //citim fiecare pereche de muchii
        cin >> x >> y;
        A[x][y] = A[y][x] = 1;
    }
}


void descompunere()
{
    int i, nr_comp_conex = 0;
    for (i = 1; i <= n; i++)
        if (!uz[i])
        {
            ++nr_comp_conex;
            dfs_matrice(i);
        }
    if (k >= nr_comp_conex && k < n)
        cout << "Exista o partitie.\n";
    else
        cout << "Nu exista o partitie.\n";
}


void dfs_matrice(int x)
{
    int i;
    uz[x] = 1;
    for (i = 0; i < n; i++)
        if (A[x][i] == 1 && uz[i] == 0)
            dfs_matrice(i);
}