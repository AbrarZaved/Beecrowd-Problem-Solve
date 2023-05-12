#include<stdio.h>
#include<math.h>
void Hoho(int a,int b)
{
    int c=24;
    if(a>12 && b<12)
    printf("O JOGO DUROU %d HORA(S)\n",(c-a)+b);
    else if(a==0 && b==0)
    printf("O JOGO DUROU %d HORA(S)\n",c);
    else if(((a>12 && b>12) &&(a>b)))
    printf("O JOGO DUROU %d HORA(S)",b-a);
    else if((a<12 && b>12)
    //printf("O JOGO DUROU %d HORA(S)",b-a);

}
int main()
{
    int x,y;
    scanf("%d%d",&x,&y);
    Hoho(x,y);
}