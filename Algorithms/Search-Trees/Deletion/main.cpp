void stergere(Arbore &rad, int x)
    {//il caut pe x
     Arbore p, t, pmin, tmin, f;
     p=rad; t=NULL;
     while (p)
            {if (p->inf==x)
                 break;
             if (x<p->inf)
                 {t=p;
                  p=p->st;
                 }
                 else
                 {t=p;
                  p=p->dr;
                 }
            }
     if (!p)
         return ;
     if (p->st && p->dr)
         {//caut minimul din dreapta
          pmin=p->dr; tmin=p;
          while (pmin->st)
                 {tmin=pmin;
                  pmin=pmin->st;
                 }
          p->inf=pmin->inf;
          p=pmin; t=tmin;
         }
     if (p->st)
         f=p->st;
         else
         f=p->dr;
     if (!t)
         rad=f;
         else
         {if (t->st==p)
              t->st=f;
              else
              t->dr=f;
         }
     delete p;
    }
