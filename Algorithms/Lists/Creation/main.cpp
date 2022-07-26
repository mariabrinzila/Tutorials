#include <fstream>

using namespace std;

ifstream fin("liste.in");
ofstream fout("liste.out");

struct nod
      {
       int inf;
       struct nod *urm;
      };

typedef struct nod *LSI;

LSI ListaStiva, ListaCoada, ListaOrdonata, L1, L2, L3;
nod *capat;

void inserare(LSI &L, int x, nod *p);
void parcurgere(LSI L);
void stergere(LSI &L, nod *p);
void creareStiva(LSI &stiva);
void creareCoada(LSI &coada, nod *&capat);
void creareOrdonata(LSI &lista);
LSI interclasare1(LSI L1, LSI L2);
LSI interclasare2(LSI L1, LSI L2);

int main()
{/*creareStiva(ListaStiva);
 parcurgere(ListaStiva);
 creareCoada(ListaCoada, capat);
 parcurgere(ListaCoada);
 creareOrdonata(ListaOrdonata);
 parcurgere(ListaOrdonata); */
 creareOrdonata(L1); creareOrdonata(L2);
 L3=interclasare2(L1, L2);
 parcurgere(L3);
 return 0;
 fin.close();
 fout.close();
}


void inserare(LSI &L, int x, nod *p)
    {nod *q=new nod;
     q->inf=x;
     if (p==NULL)
         {q->urm=L;
          L=q;
         }
         else
         {q->urm=p->urm;
          p->urm=q;
         }
    }


void parcurgere(LSI L)
    {nod *it;
     if (L==NULL)
         return ;
     for (it=L; it!=NULL; it=it->urm)
          fout<<it->inf<<' ';
     fout<<'\n';
    }


void stergere(LSI &L, nod *p)
    {LSI q;
     if (p==NULL)
         {q=L;
          if (q)
              {L=L->urm;
               delete q;
              }
         }
         else
         {q=p->urm;
          if (q)
              {p->urm=q->urm;
               delete q;
              }
         }
    }


void creareStiva(LSI &stiva)
    {int i, n, val;
     fin>>n;
     for (i=1; i<=n; i++)
          {fin>>val;
           inserare(stiva, val, NULL);
          }
    }


void creareCoada(LSI &coada, nod *&capat)
    {int i, n, val;
     capat=NULL;
     fin>>n; fin>>val;
     inserare(coada, val, capat);
     capat=coada;
     for (i=2; i<=n; i++)
          {fin>>val;
           inserare(coada, val, capat);
           capat=capat->urm;
          }
    }


void creareOrdonata(LSI &lista)
    {int i, n, val;
     nod *curent, *next;
     fin>>n; fin>>val;
     inserare(lista, val, NULL);
     for (i=2; i<=n; i++)
          {fin>>val;
           if (lista->urm==NULL)
               {if (val<lista->inf)
                    inserare(lista, val, NULL);
                    else
                    inserare(lista, val, lista);
                continue;
               }
           if (val<lista->inf)
               {inserare(lista, val, NULL);
                continue;
               }
           curent=lista;
           next=curent->urm;
           for (; next!=NULL; curent=curent->urm, next=next->urm)
                if (val<next->inf)
                    break;
           inserare(lista, val, curent);
          }
    }


LSI interclasare1(LSI L1, LSI L2)
   {nod *p, *q, *curent=NULL;
    LSI L3=NULL;
    if (!L1)
        return L2;
    if (!L2)
        return L1;
    p=L1; q=L2;
    if (p->inf<q->inf)
        {inserare(L3, p->inf, curent);
         p=p->urm;
         curent=L3;
        }
        else
        {inserare(L3, q->inf, curent);
         q=q->urm;
         curent=L3;
        }
    while (p!=NULL && q!=NULL)
           {while (p && p->inf<q->inf)
                   {inserare(L3, p->inf, curent);
                    p=p->urm;
                    curent=curent->urm;
                   }
            while (p && q && q->inf<p->inf)
                   {inserare(L3, q->inf, curent);
                    q=q->urm;
                    curent=curent->urm;
                   }
           }
    while (p)
           {inserare(L3, p->inf, curent);
            p=p->urm; curent=curent->urm;
           }
    while (q)
           {inserare(L3, q->inf, curent);
            q=q->urm; curent=curent->urm;
           }
    return L3;
   }


LSI interclasare2(LSI L1, LSI L2)
   {LSI L3;
    nod *p, *q, *aux;
    if (!L1)
        return L2;
    if (!L2)
        return L1;
    if (L1->inf<L2->inf)
        {p=L1; L3=L1;
         q=L2;
        }
        else
        {p=L2; L3=L2;
         q=L1;
        }
    while (q)
           {while (p->urm && p->urm->inf<=q->inf)
                   p=p->urm;
            aux=p->urm;
            p->urm=q;
            q=aux;
           }
    return L3;
   }
