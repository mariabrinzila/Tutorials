void inserare(Arbore &rad, int x)
    {if (rad==NULL)
         {rad=new nodA;
          rad->inf=x;
          rad->st=NULL; rad->dr=NULL;
         }
         else
         {if (x==rad->inf)
              return ;
          if (x<rad->inf)
              inserare(rad->st, x);
          if (x>rad->inf)
              inserare(rad->dr, x);
         }
    }
