bool cautare1(Arbore rad, int lo, int hi)
    {if (!rad)
         return 1;
     if (rad->inf<lo || rad->inf>hi)
         return 0;
     return (cautare(rad->st, lo, rad->inf-1) && cautare(rad->dr, rad->inf+1, hi));
    }


bool cautare2(Arbore rad)
    {if (rad==NULL)
         return 1;
     if (rad->st!=NULL && maxim(rad->st)->inf>=rad->inf)
         return 0;
     if (rad->dr!=NULL && minim(rad->st)->inf<=rad->inf)
         return 0;
     return 1;
    }


Arbore maxim(Arbore rad)
      {while (rad->dr)
              rad=rad->dr;
       return rad;
      }


Arbore minim(Arbore rad)
      {while (rad->st)
              rad=rad->st;
       return rad;
      }
