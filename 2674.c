#include<stdio.h>
int main()
{
    int a,rem,count=0;
    scanf("%d",&a);
    while(a>0)
    {
        rem=a%10;
        a=a/10;
        if(rem==2 || rem==3 || rem==5 || rem==7)
        count++;
        else
        count=-1;
    }

    if(count>1)
    printf("Super\n");
    else if(count==-1)
    printf("Primo\n");     
}