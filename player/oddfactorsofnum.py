#include<stdio.h>
int main()
{
    int n,i;
    printf("enter the value");
    scanf("%d",&n);
    if(n<=3)
    {
        printf("\n no odd factor ");
    }
    else
    {
        printf("the odd factor ");
        for(i=3;i<n;i++)
        {
            if(n%i==0)
            {
                printf("%d",i);
            }
        }
    }
    return 0;
    
    
    
    
}
