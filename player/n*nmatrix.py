#include<stdio.h>
void main()
{
int a[10][10],i,j,n,d,sum=1,num=1;
printf("enterr the n value:\t");
scanf("%d",&n);
printf("enter the array values:");
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)  
{
scanf("%d\t",&a[i][j]);    
}printf("\n");
}
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)
{
 if(i==j)
 {
     sum=sum*(a[i][j]);
 }
}
}
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)
{
 if((i+j)==(n+1))
 {
     num=num*(a[i][j]);
 }
}
}
printf("%d\n%d",sum,num);
d=sum+num;
printf("\nthe product of sum of diagonals are:%d",d);
}
