#include<stdio.h>
int main()
{
int a[20],b[20],i,j,n,temp,flag=0;
printf("enter number of elements in array");
scanf("%d",&n);
printf("Enter an array");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
b[i]=a[i];
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]>a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
for(i=0;i<n;i++)
{
    if(a[i]!=b[i])
    {
        flag=1;
    }
}
if(flag==0)
{
    printf("\nYes");
}
else
{
    printf("\nNo");
}
return 0;



}
