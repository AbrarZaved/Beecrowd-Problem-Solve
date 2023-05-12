#include<stdio.h>
int main()
{
    int i=1,j=7,count=1;
    while(i<=9)
    {   
        while(count<=3)
        {
            
            printf("I=%d J=%d\n",i,j);
            count++;
            j--;

        }

        i=i+2;
        count=1;
        j=7;
        
        
    }
    return 0;
}