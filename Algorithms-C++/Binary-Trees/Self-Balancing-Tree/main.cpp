bool echilibrat(Arbore rad)
    {if (rad==0)
		 return 1;
	 int a=numara(rad->st);
	 int b=numara(rad->dr);
	 if (abs(a,b)<=1)
         return echilibrat(rad->st) && echilibrat(rad->dr);
	 return 1;
    }


int numara(Arbore rad)
   {if (rad==NULL)
        return 0;
    return 1+numara(rad->st)+numara(rad->dr);
   }


int abs(int a, int b)
   {if (a>b)
        return a-b;
    return b-a;
   }

