#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    cin.ignore();
    while(t--)
    {
        string a,b;
        cin>>a>>b;
        int i=0,c;
        int e = b.length();
        int d = a.length();
        if(e>d || e==d)
        c=e;
        else
        c=d;
        while(c--)
        {
            cout<<a[i];
            cout<<b[i];
            i++;
        }
        cout<<endl;
    }


}