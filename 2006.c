#include<stdio.h>
int main()
{
    int n,a[5],i,count=0;
    scanf("%d",&n);
    for(i=0;i<5;i++)
    scanf("%d",&a[i]);
    for(i=0;i<5;i++)
    {   
        if(a[i]==n)
        count++;

    }

    printf("%d\n",count);

}