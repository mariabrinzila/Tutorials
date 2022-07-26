#include <fstream>
#define NMAX 1000

using namespace std;

ifstream fin("sort.in");
ofstream fout("sort.out");

int n;
int a[NMAX], b[NMAX];

void citire();
void msort(int st, int dr);
void interclasare(int st, int dr);
void afisare();

int main()
{citire();
 msort(1, n);
 afisare();
 return 0;
 fin.close();
 fout.close();
}


void citire()
    {int i;
     fin>>n;
     for (i=1; i<=n; i++)
          fin>>a[i];
    }


void msort(int st, int dr)
    {int mij;
     if (st<dr) //macar 2 elemente
         {mij=(st+dr)/2;
          msort(st, mij);
          msort(mij+1, dr);
          interclasare(st, dr);
         }
    }


void interclasare(int st, int dr)
    {int is, id, mij, ib;
     mij=(st+dr)/2;
     is=st; id=mij+1; ib=st;
     while (is<=mij && id<=dr)
            if (a[is]<a[id])
                b[ib++]=a[is++];
                else
                b[ib++]=a[id++];
     while (is<=mij)
            b[ib++]=a[is++];
     while (id<=dr)
            b[ib++]=a[id++];
     //copiez rez din b in a
     for (ib=st; ib<=dr; ib++)
          a[ib]=b[ib];
    }


void afisare()
    {int i;
     for (i=1; i<=n; i++)
          fout<<a[i]<<' ';
    }
