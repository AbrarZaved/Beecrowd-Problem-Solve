#include<stdio.h>
void hudai(int a)
{
    int n, i,j = 1,k = 2,l = 3;
    //scanf("%d", &n);
    for(i = 1;i <= a;i++){
        printf("%d %d %d\n",i, (i*i), (i*i*i));
        printf("%d %d %d\n",i, (i*i) + 1, (i*i*i) + 1);
    }

}

int main()
{
    int b;
    scanf("%d",&b);
    hudai(b);

}