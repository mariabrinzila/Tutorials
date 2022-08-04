#include <iostream>

using namespace std;

int n, sum;
int p[100];

void gen(int k);

int main()
{cout<<"n="; cin>>n;
 p[0]=1;
 gen(1);
 return 0;
}


void gen(int k)
    {int i;
     if (sum==n)
         {for (i=1; i<k; i++)
               cout<<p[i];
          cout<<'\n';
         }
         else
         for (i=p[k-1]; i<=n-sum; i++)
              {p[k]=i; sum+=i;
               gen(k+1);
               sum-=i;
              }
    }
