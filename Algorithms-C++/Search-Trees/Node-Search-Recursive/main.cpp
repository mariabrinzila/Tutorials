Arbore cautare(Arbore rad, int x)
      {if (rad==NULL)
           return NULL;
       if (rad->inf==x)
           return rad;
       if (x<rad->inf)
           return cautare(rad->st, x);
       return cautare(rad->dr, x);
      }
