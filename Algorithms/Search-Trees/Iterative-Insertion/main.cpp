void inserare(Arbore &rad, int x)
    {Arbore p, q;
     if (rad==NULL)
         {rad=new nodA;
          rad->inf=x;
          rad->st=NULL; rad->dr=NULL;
         }
         else
         {p=rad;
          while (1)
                 {if (x==p->inf)
                      break;
                  if (x<p->inf)
                      {if (p->st==NULL)
                           {q=new nodA;
                            q->inf=x;
                            q->st=NULL; q->dr=NULL;
                            p->st=q; break;
                           }
                           else
                           p=p->st;
                      }
                  if (x>p->info)
                      {if (p->dr==NULL)
                           {q=new nodA;
                            q->inf=x;
                            q->st=NULL; q->dr=NULL;
                            p->dr=q; break;
                           }
                           else
                           p=p->dr;
                      }
                 }
         }
    }
