#include<stdio.h>
struct Apple{
    int a[500];
    double b[800];
    char c[1000];
}a1, a2;
int main(){
    printf("Size of a1: %d\n", sizeof(a1));
    return 0;
}
