#include <iostream>
#include <cstring>
#define LMAX 1001

using namespace std;

char s1[LMAX], s2[LMAX];

void nrap(char s1[LMAX], char s2[LMAX]);
void stergere(char s1[LMAX], char s2[LMAX]);

int main()
{cin.getline(s1, LMAX); cin.getline(s2, LMAX);
 nrap(s1, s2);
 stergere(s1, s2);
 return 0;
}

//numaram nr aparitii a lui s2 in s1
void nrap(char s1[LMAX], char s2[LMAX])
    {int ap=0, i, lg;
     char *p;
     lg=strlen(s2); p=strstr(s1, s2);
     while (p)
            {ap++;
             p=strstr(p+1, s2);
            }
     cout<<ap;
    }


//stergem aparitiile lui s2 din s1
void stergere(char s1[LMAX], char s2[LMAX])
    {int lg;
     char *p;
     lg=strlen(s2); p=strstr(s1, s2);
     while (p)
            {strcpy(p, p+lg);
             p=strstr(p, s2);
            }
     cout<<s1;
    }
