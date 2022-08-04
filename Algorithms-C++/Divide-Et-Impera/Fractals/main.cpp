#include <iostream>
#include "graphics2.h"
#include <cstring>

using namespace std;

char c;
void fractal(int L, int xc, int yc, bool niv);

int main()
{//initializare mod grafic
 int L=250, xc, yc;
 int driver, mod;
 initgraph(&driver, &mod, "", 1024, 768); //ultimii 2 parametri = dimensiunea in pixeli a ferestrei grafice
 //desenez
 xc=getmaxx()/2; yc=getmaxy()/2;
 fractal(L, xc, yc, 0);
 while (!kbhit());
 //gata
 closegraph();
 return 0;
}


void fractal(int L, int xc, int yc, bool niv)
    {if (L>1)
         {fractal(L/2, xc-L/2, yc-L/2, !niv);
          fractal(L/2, xc-L/2, yc+L/2, !niv);
          fractal(L/2, xc+L/2, yc-L/2, !niv);
          fractal(L/2, xc+L/2, yc+L/2, !niv);
          if (niv==0)
              {setcolor(RED);
               setfillstyle(SOLID_FILL, RED);
              }
              else
              {setcolor(BLUE);
               setfillstyle(SOLID_FILL, BLUE);
              }
          bar(xc-L/2, yc-L/2, xc+L/2, yc+L/2);
          setcolor(YELLOW);
          rectangle(xc-L/2, yc-L/2, xc+L/2, yc+L/2);
         }
    }
