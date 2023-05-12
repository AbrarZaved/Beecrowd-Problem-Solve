#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int italic=0,bold=0,count=0,hudai=0;
    string a;
    getline(cin,a);
    for(int i=0;i<a.length();i++)
    {
        if(a[i]=='_')
        ++italic;
        if(a[i]=='*')
        ++bold;
        if(italic%2!=0 && italic!=0 && count==0){
        cout<<"<i>";
        count=1;
        }
        else if(italic%2==0 && italic!=0 && count==1){
        cout<<"</i>";
        count=0;
        }
        else if(bold%2!=0 && bold!=0 && hudai==0){
        cout<<"<b>";
        hudai=1;
        }
        else if(bold%2==0 && bold!=0 && hudai==1){
        cout<<"</b>";
        hudai=0;
        }
        
        else
        cout<<a[i];

       


    }
}