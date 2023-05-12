#include<stdio.h>
void Animal()
{
    char a[20],b[20],c[20];
    gets(a);
    gets(b);
    gets(c);
    if(a[0]=='v' && b[0]=='a' && c[0]=='c')
    printf("aguia\n");
    else if(a[0]=='v' && b[0]=='a' && c[0]=='o')
    printf("pomba\n");
    else if(a[0]=='v' && b[0]=='m' && c[0]=='o')
    printf("homem\n");
    else if(a[0]=='v' && b[0]=='m' && c[0]=='h')
    printf("vaca\n");
    else if(a[0]=='i' && b[0]=='i' && c[0]=='h')
    printf("pulga\n");
    else if(a[0]=='i' && b[0]=='i' && c[2]=='r')
    printf("lagarta\n");
    else if(a[0]=='i' && b[0]=='a' && c[0]=='h')
    printf("sanguessuga\n");
    else
    printf("minhoca\n");

}
int main()
{
    Animal();
}