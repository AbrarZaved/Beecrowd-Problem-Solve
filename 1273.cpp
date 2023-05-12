#include<iostream>
#include<string.h>
#include<climits>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while (t!=0)
    {
        int maxNo=0;
        string a[t];
        for(int i=0;i<t;i++)
        cin>>a[i];

        for(i=0;i<t;i++)
             maxNo=max(maxNo,a[i].length());
        
         cout<<maxNo<<endl;
        break;
     
    
    

    }
    
}