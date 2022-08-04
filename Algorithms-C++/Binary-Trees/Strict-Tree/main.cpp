bool strict(Arbore rad)
    {if (rad==0)
	  	 return 1;
     if (!(rad->st) && !(rad->dr))
         return 1;
     if (rad->st && rad->dr)
         return (strict(rad->st) && strict(rad->dr));
     return 0;
    }
