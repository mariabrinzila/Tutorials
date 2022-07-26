int inaltime(Arbore rad)
   {int stanga=0, dreapta=0;
    if (rad==NULL)
        return -1;
    stanga=inaltime(rad->st);
    dreapta=inaltime(rad->dr);
    return 1+max(stanga, dreapta);
   }
