#include<stdio.h>
int main()
{
    int a,count=0,b=0,c=0;
    while(a!=4)
    {
        scanf("%d",&a);
        if(a==1)
        count++;
        else if(a==2)
        b++;
        else if(a==3)
        c++;

    }
    
    printf("Muito Obrigado\n");
    printf("Alcool: %d\n",count);
    printf("Gasolina: %d\n",b);
    printf("Diesel: %d\n",c);

    return 0;
    
}