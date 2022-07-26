#include <iostream>
#include "graphics2.h"

using namespace std;

void sierpinski(int, int, int, int, int, int, int);

int main()
{
    // initializare
    int driver, mod;
    initgraph(&driver, &mod, "", 1024, 768);

    int poly[8];
    poly[0] = 100;
    poly[1] = 700;
    poly[2] = 510;
    poly[3] = 50;
    poly[4] = 930;
    poly[5] = 700;
    poly[6] = poly[0];
    poly[7] = poly[1];
    // desenez
    sierpinski(poly[0], poly[1], poly[2], poly[3], poly[4], poly[5], 0);
    while (!kbhit());

    // gata
    closegraph();
    return 0;
}

void sierpinski(int x1, int y1, int x2, int y2, int x3, int y3, int iter)
{
    if (iter < 10)
    {
        int mx1 = (x1 + x2) / 2, my1 = (y1 + y2) / 2;
        int mx2 = (x2 + x3) / 2, my2 = (y2 + y3) / 2;
        int mx3 = (x3 + x1) / 2, my3 = (y3 + y1) / 2;
        int a[8] = { x1, y1, x2, y2, x3, y3, x1, y1 };
        int b[8] = { mx1, my1, mx2, my2, mx3, my3, mx1, my1 };

        setcolor(YELLOW);
        drawpoly(4, a);
        setfillstyle(SOLID_FILL, RED);
        fillpoly(4, b);
        setfillstyle(SOLID_FILL, BLUE);
        fillpoly(4, b);

        sierpinski(x1, y1, mx1, my1, mx3, my3, iter + 1);
        sierpinski(mx1, my1, x2, y2, mx2, my2, iter + 1);
        sierpinski(mx3, my3, mx2, my2, x3, y3, iter + 1);
    }
}
