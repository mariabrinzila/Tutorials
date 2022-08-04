#include <fstream>
#define LGMAX 1000

using namespace std;

ifstream fin("nrmari.in");
ofstream fout("nrmari.out");

typedef int NrMare[LGMAX];

void suma(NrMare a, int lga, NrMare b, int lgb, NrMare c, int& lgc);
void umplezero(NrMare x, int poz1, int poz2);
void citire(NrMare x, int& lgx);
void afisare(NrMare x, int lgx);

int main()
{NrMare x, y, z;
 int lgx, lgy, lgz;
 citire(x, lgx);
 citire(y, lgy);
 suma(x, lgx, y, lgy, z, lgz);
 afisare(z, lgz);
 return 0;
}

void afisare(NrMare x, int lgx)
    {int i;
     for (i=lgx-1; i>=0; i--)
          fout<<x[i];
    }

void citire(NrMare x, int& lgx)
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

void suma(NrMare a, int lga, NrMare b, int lgb, NrMare c, int& lgc)
    {int i, t, aux;
     if (lga<lgb)
         {umplezero(a, lga, lgb);
          lgc=lgb;
         }
         else
         {umplezero(b, lgb, lga);
          lgc=lga;
         }
     for (i=t=0; i<lgc; i++)
          {aux=a[i]+b[i]+t;
           c[i]=aux%10;
           t=aux/10;
          }
     if (t)
         c[lgc++]=t;
    }

void umplezero(NrMare x, int poz1, int poz2)
    {int i;
     for (i=poz1; i<poz2; i++)
          x[i]=0;
    }
