#include<stdio.h>
int main()
{
    int x,y,i,a=2,b;
    scanf("%d%d",&x,&y);
    b=x;
    for(i=1;i<y;i++)
    {   
        printf("%d ",i);
        if(i==b)
        {   
            printf("\n");
            b=x*a;
            a++;
        }     
        
    }
}