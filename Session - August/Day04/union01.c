#include<stdio.h>
union Apple{
    int a[300];
    float b[100];
    char c[101];
}a1, a2;
int main(){
    printf("Size of a1: %d\n", sizeof(a1));
    return 0;
}
