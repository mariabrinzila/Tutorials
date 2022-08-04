int frunze(Arbore rad)
   {if (rad==NULL)
        return 0;
    if (rad->st==NULL && rad->dr==NULL)
        return 1;
    return frunze(rad->st)+frunze(rad->dr);
   }
