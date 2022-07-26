# include <iostream>
using namespace std;

int n, x[25005], m, y[200005];

int caut(int st, int dr, int v[], int x)
{
    if(st > dr)
            return 0;
    else
    {
        int m = (st + dr)/2;
        if(v[m] == x)
            return m;
        if(v[m] > x)
            return caut(1, m-1, v, x);
        if(v[m] < x)
            return caut(m+1, dr, v, x);
        return 0;
    }
}

void citire(int &n, int v[])
{
    cin>>n;
    for(int i = 1; i <= n ; i++)
        cin>>v[i];
}

int main()
{
    citire(n, x);
    citire(m, y);
    for(int i=1; i<=m; i++)
           if((caut(1, n, x, y[i])))
              cout<<1<<" ";
            else
                cout<<0<<" ";

    return 0;
}
