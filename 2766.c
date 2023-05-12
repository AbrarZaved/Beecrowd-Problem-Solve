#include<stdio.h>
int main()
{
    int i=0;
    char b[30];
    while(i<=10)
    {
    scanf("%s",b);
    if(i==3||i==7||i==9)
    printf("%s\n",b);
    i++;
    }
    return 0;



}
