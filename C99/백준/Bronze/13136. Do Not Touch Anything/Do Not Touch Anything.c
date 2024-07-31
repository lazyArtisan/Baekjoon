#include <stdio.h>

int main() {
    long long H, W, N, H_need, W_need, R;
    scanf("%d %d %d", &H, &W, &N);
    H_need = H%N == 0 ? H/N : H/N + 1;
    W_need = W%N == 0 ? W/N : W/N + 1;
    printf("%lld",H_need*W_need);
}