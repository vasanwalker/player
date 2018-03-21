#include <stdio.h>
int main(void){
	int a[5],b[5],i,d=0,c[5],k=1;

	for(i=1;i<=5;i++)
	{
	scanf("%d",&a[i]);
	}
	for(i=1;i<=5;i++)
	{
	scanf("%d",&b[i]);	
	}
	for(i=5;i>=1;i--)
	{
		c[k]=a[i];
		k++;
	}
	for(i=1;i<=5;i++)
	{
		if(c[i]==b[i])
	             { d++;
	}}
	if(d==5)
	{
		printf("yes");
	}
	return 0;
  
  
  
  
  
  
  
}
