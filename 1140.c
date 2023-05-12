#include<stdio.h>
#include<string.h>
int main()
{
    char sent[1000];
    int y=0,n=0;
    gets(sent);
    int a=strlen(sent);
    strlwr(sent);
    char c=sent[0];
    for(int i=0;i<a;i++)
    {
        if(sent[i]==' ' && sent[i+1]!=c){
            n++;
            y=0;
            break;
        }
        else{
        y++;
        n=0;
        }
    }
    if(n==0)
    printf("Yes\n");
    else 
    printf("No\n");
}
