#include <iostream>

using namespace std;

typedef int Huge[25];

void read(Huge x, int& lgx);
unsigned long Mod(Huge A, int lga, unsigned long X);

Huge A;
int lga, R;

int main()
{read(A, lga);
 R=Mod(A, lga, 11);
 cout<<R;
 return 0;
}


void read(Huge x, int& lgx)
{char c;
     int st, dr, aux;
     lgx=0;
     do {cin.get(c);
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


unsigned long Mod(Huge A, int lga, unsigned long X)
{ int i;
  unsigned long R=0;
  for (i=lga-1;i>=0;i--)
    R=(10*R+A[i])%X;
  return R;
}
