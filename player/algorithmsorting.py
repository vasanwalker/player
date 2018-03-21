#include<stdio.h>
int main() 
{
   int n,i,a[100],t,j;
   scanf("%d",&n);
   for(i=0;i<n;i++)
   {
       scanf("%d",&a[i]);
   }
   for(i=0;i<(n-1);i++)
   for(j=0;j<(n-i-1);j++)
   {
       if(a[j]<a[j+1])
       {
           t=a[j];
           a[j]=a[j+1];
           a[j+1]=t;
       }
   }if(n%2==0)
   {
        for(i=0;i<n/2;i++)
        {
            printf("%d %d ",a[i],a[n-i-1]);
        }
   }else
   {
      for(i=0;i<n/2;i++)
        {
            printf("%d %d ",a[i],a[n-i-1]);
        }printf("%d",a[n/2]); 
   }
}
