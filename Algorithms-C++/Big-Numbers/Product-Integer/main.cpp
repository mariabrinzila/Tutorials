#include <fstream>
#define LGMAX 1000

using namespace std;

ifstream fin("nrmari.in");
ofstream fout("nrmari.out");

typedef int nrMare[LGMAX];

void umplezero(nrMare x, int poz1, int poz2);
void citire(nrMare x, int& lgx);
void afisare(nrMare x, int lgx);
void prod(nrMare x, int lgx, int a, nrMare y, int& lgy);

int main()
{nrMare x, y, z;
 int lgx, lgy, lgz;
 citire(x, lgx);
 citire(y, lgy);
 prod(x, lgx, 1, x, lgx);
 afisare(x, lgx);
 return 0;
}

void afisare(nrMare x, int lgx)
    {int i;
     for (i=lgx-1; i>=0; i--)
          fout<<x[i];
    }

void citire(nrMare x, int& lgx)
    {char c;
     int st, dr, aux;
     lgx=0;
     do {fin.get(c);
         if (c=='\n')
             break;
             else
             x[lgx++]=c-'0';
        }
     while (1);
     for (st=0, dr=lgx-1; st<dr; st++, dr--)
          {aux=x[st];
           x[st]=x[dr];
           x[dr]=aux;
          }
    }

void umplezero(nrMare x, int poz1, int poz2)
    {int i;
     for (i=poz1; i<poz2; i++)
          x[i]=0;
    }

void prod(nrMare x, int lgx, int a, nrMare y, int& lgy)
    {int i, t=0, aux;
     if (a==0 || (x[0]==0 && lgx==1))
         {y[0] = 0; lgy = 1;
          return ;
         }
     for (i=0; i<lgx; i++)
          {aux=x[i]*a+t;
           y[i]=aux%10;
           t=aux/10;
          }
     lgy=lgx;
     while (t)
            {y[lgy++]=t%10;
             t/=10;
            }
    }
