Arbore copie(Arbore rad)
      {Arbore p;
       if (rad==NULL)
           return 0;
       p=new nodA;
       p->inf=rad->inf;
       p->st=copie(rad->st);
       p->dr=copie(rad->dr);
       return p;
      }
