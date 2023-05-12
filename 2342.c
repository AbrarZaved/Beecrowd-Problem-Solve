#include<stdio.h>
int main()
{
    int a,b,c,total;
    char d;
    scanf("%d%d%c%d",&a,&b,&d,&c);
    if(d=='+')
    total=b+c;
    else if(d=='*')
    total=b*c;
    if(total<=a)
    printf("OK\n");
    else
    printf("OVERFLOW\n");
    return 0;
}