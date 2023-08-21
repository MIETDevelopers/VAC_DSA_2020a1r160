#include <stdio.h>
int main()
{
    int a = 3;
    int b = 5;
    b = ++a + ++a;
    printf("%d %d", a, b);
    return 0;
}