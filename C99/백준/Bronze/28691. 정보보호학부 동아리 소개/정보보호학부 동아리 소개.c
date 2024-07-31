#include <stdio.h>

int main() {
    char C;
    scanf("%c", &C);
    if (C == 'M')
        printf("MatKor");
    else if (C == 'W')
        printf("WiCys");
    else if (C == 'C')
        printf("CyKor");
    else if (C == 'A')
        printf("AlKor");
    else
        printf("$clear");
}