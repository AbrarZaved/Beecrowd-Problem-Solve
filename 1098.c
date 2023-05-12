#include<stdio.h>
int main()
{
    float i=0,j=1,count=1,total=0;
    int a=1,b=1;
    for(int k=0;k!=2;k++)
    {   
        while(count<=3)
        {
            if(total==0){
            printf("I=%d J=%d\n",a,b);
            b++;
            }
            else{
            printf("I=%.1f J=%.1f\n",i,i+j);
            j++;
            }
            count++;



        }
        a++;
        i=i+.2;
        count=1;
        j=1;
        
        
    }
    return 0;
}