#include <iostream>
#define NMAX 1000

using namespace std;

struct nodA
      {
       int inf;
       struct nodA *st, *dr;
      };

typedef nodA *Arbore;

Arbore rad;
Arbore C[NMAX];
int prim, ultim;

Arbore creareArbore();
void preordine(Arbore rad);
void postordine(Arbore rad);
void inordine(Arbore rad);
void niveluri(Arbore rad);

int main()
{rad=creareArbore();
 preordine(rad); cout<<'\n';
 //postordine(rad); cout<<'\n';
 //inordine(rad); cout<<'\n';
 niveluri(rad); cout<<'\n';
 return 0;
}


Arbore creareArbore()
      {Arbore p=new nodA;
       int raspuns;
       cout<<"Introduceti informatia nodului ";
       cin>>p->inf;
       cout<<"Exista fiu stang? (0/1)";
       cin>>raspuns;
       if (raspuns==0)
           p->st=NULL;
           else
           p->st=creareArbore();
       cout<<"Exista fiu drept? (0/1)";
       cin>>raspuns;
       if (raspuns==0)
           p->dr=NULL;
           else
           p->dr=creareArbore();
       return p;
      }



void preordine(Arbore rad)
    {if (rad)
         {cout<<rad->inf<<' ';
          preordine(rad->st);
          preordine(rad->dr);
         }
    }


void postordine(Arbore rad)
    {if (rad)
         {postordine(rad->st);
          postordine(rad->dr);
          cout<<rad->inf<<' ';
         }
    }


void inordine(Arbore rad)
     {if (rad)
         {inordine(rad->st);
          cout<<rad->inf<<' ';
          inordine(rad->dr);
         }
    }


void niveluri(Arbore rad)
     {nodA *p;
      prim=ultim=1; C[1]=rad;
      while (prim<=ultim)
             {p=C[prim++];
              cout<<p->inf<<' ';
              if (p->st)
                  C[++ultim]=p->st;
              if (p->dr)
                  C[++ultim]=p->dr;
             }
     }
