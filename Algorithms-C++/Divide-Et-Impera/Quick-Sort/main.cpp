#include <fstream>
#define NMAX 1000

using namespace std;

ifstream fin("sort.in");
ofstream fout("sort.out");

int n;
int a[NMAX];

void citire();
void qsort(int st, int dr);
int divide(int st, int dr);
void afisare();

int main()
{citire();
 qsort(1, n);
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


void qsort(int st, int dr)
    {int poz;
     if (st<dr) //macar 2 elemente
         {poz=divide(st, dr);
          qsort(st, poz-1);
          qsort(poz+1, dr);
         }
    }


int divide(int st, int dr)
   {int pivot=a[st];
    int i=st, j=dr;
    while (i<j)
           {//liber la stanga
            while (i<j && a[j]>=pivot)
                   j--;
            a[i]=a[j];
            //liber la dreapta
            while (i<j && a[i]<=pivot)
                   i++;
            a[j]=a[i];
           }
    a[i]=pivot;
    return i;
   }


void afisare()
    {int i;
     for (i=1; i<=n; i++)
          fout<<a[i]<<' ';
    }
