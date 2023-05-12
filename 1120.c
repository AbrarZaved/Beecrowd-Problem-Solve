#include<stdio.h>
#include<string.h>
int main()
{
    char n;
    char a[1000];
    scanf("%c",&n);
    //scanf("%d",&n);
    gets(a);
    int b = strlen(a);
    int i;
    for(i=1;i<=b;i++)
    {
        
        if(a[i]!=n)
        printf("%c",a[i]);
        else
        //printf("0");
    }
}