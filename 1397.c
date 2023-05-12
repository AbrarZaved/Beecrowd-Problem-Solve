#include<stdio.h>
int main()
{
    int n,a[10],b[10],i,j,c=0,d=0,count=0;
    while(n>0)
    {
        scanf("%d",&n);
        for(i=0,j=0;i<n,j<n;i++,j++)
        {
           scanf("%d%d",&a[i],&b[j]);
           if(a[i]>b[j])
           c++;
           else if(a[i]<b[j])
           d++;

        }
        if(n==0)
        return 0;
        else
        printf("%d %d\n",c,d); 
            c=0;
            d=0;
        
    }

    


}