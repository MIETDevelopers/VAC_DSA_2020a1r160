#include <stdio.h>
#include <string.h>

void buildString(char *s) {
    char result[1000];
    int len = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != '#') {
            result[len] = s[i];
            len++;
        } else if (len > 0) {
            len--;
        }
    }

    result[len] = '\0';

    strcpy(s, result);
}

int backspaceCompare(char *S, char *T) {
    buildString(S);
    buildString(T);

    return strcmp(S, T) == 0;
}

int main() {
    char S[1000];
    char T[1000];

    printf("S: ");
    scanf("%s", S);

    printf("T: ");
    scanf("%s", T);

    if (backspaceCompare(S, T)) {
        printf("True\n");
    } else {
        printf("False\n");
    }

    return 0;
}
