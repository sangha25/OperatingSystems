#include<stdio.h>
void main()
{
int pid;
pid=fork();
if(pid>0)
{
 printf("\n child : %d",getpid());
}
else if(pid==0)
{
printf("\n parent : %d",getpid());
printf("\n parent : %d",getppid());
}
}

