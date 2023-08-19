#include<stdio.h>
struct Apple{
    int a[100];
    float b[500];
    char c[777];
}a1, a2;
int main(){
    printf("Size of a1: %d\n", sizeof(a1));
    return 0;
}
