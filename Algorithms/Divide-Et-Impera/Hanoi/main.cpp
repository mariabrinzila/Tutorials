#include <fstream>

using namespace std;

ifstream fin("hanoi.in");
ofstream fout("hanoi.out");

void hanoi(int n, int ti, int tf);

int n;

int main()
{fin>>n;
 hanoi(n, 1, 2);
 return 0;
}


void hanoi(int n, int ti, int tf)
    {if (n>0)
         {hanoi(n-1, ti, 6-ti-tf);
          fout<<ti<<"->"<<tf<<'\n'; //mut baza
          hanoi(n-1, 6-ti-tf, tf);
         }
    }
