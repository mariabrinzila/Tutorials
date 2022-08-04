#include <fstream>

using namespace std;

typedef int NrMare[100];

ifstream fin("dif.in");
ofstream fout("dif.out");

NrMare n, m;
int lgn, lgm, x;

void citire(NrMare x, int& lgx);
void afisare(NrMare x, int lgx);
void dif(NrMare a, int& lga, int x, NrMare c, int& lgc);

int main()
{citire(n, lgn); fin>>x;
 dif(n, lgn, x, m, lgm);
 afisare(m, lgm);
 return 0;
 fin.close();
 fout.close();
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


void afisare(NrMare x, int lgx)
    {int i;
     for (i=lgx-1; i>=0; i--)
          fout<<x[i];
    }


void dif(NrMare a, int& lga, int x, NrMare c, int& lgc)
    {int i, t, aux;
     lgc=lga;
     for (i=t=0; i<lgc; i++)
          {aux=a[i]-x-t;
           c[i]=aux%10;
           t=aux/10;
          }
     if (t)
         c[lgc++]=t;
    }
