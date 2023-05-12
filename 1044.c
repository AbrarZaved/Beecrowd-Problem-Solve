#include<stdio.h>
void haha(int a,int b)
{
    if(a>b)
    {
        if(a%b==0)
        printf("Sao Multiplos\n");
        else
        printf("Nao sao Multiplos\n");
    }
    else
    {
        if(b%a==0)
        printf("Sao Multiplos\n");
        else
        printf("Nao sao Multiplos\n");
    }

}
int main()
{
    int x,y;
    scanf("%d%d",&x,&y);
    haha(x,y);
}