#include <stdio.h>
int main(void)
{
	int a[10],i,k=0;
 for(i=1;i<=5;i++)
 {
 	scanf("%d",&a[i]);
 }
 for(i=1;i<=5;i++)
 {
 	k=a[i]+k;
 }
 printf("%d",k);
	return 0;
}
