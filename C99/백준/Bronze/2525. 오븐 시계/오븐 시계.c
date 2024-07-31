#include <stdio.h>

int main() {
    int H, M, D, overM;
    scanf("%d %d", &H, &M);
    scanf("%d", &D);
    M = M + D;
    overM = M / 60;
    M %= 60;
    H += overM;
    H %= 24;
    printf("%d %d", H, M);
}