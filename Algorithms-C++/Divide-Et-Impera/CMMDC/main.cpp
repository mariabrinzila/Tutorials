#include <iostream>
#define VMAX 1005

using namespace std;

int v[VMAX];
int n;

void citire();
int divide(int st, int dr);
int euclid(int x, int y);

int main()
{citire();
 cout<<divide(0, n-1)<<'\n';
 return 0;
}


void citire()
    {int i;
     cin>>n;
     for (i=0; i<n; i++)
          cin>>v[i];
    }


int divide(int st, int dr)
   {int mij, js, jd;
    if (st==dr)
        return v[st];
    mij=(st+dr)/2;
    js=divide(st, mij);
    jd=divide(mij+1, dr);
    return euclid(js, jd);
   }


int euclid(int x, int y)
   {int r;
    while (y)
           {r=x%y;
            x=y;
            y=r;
           }
    return x;
   }
