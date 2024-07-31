#include <stdio.h>
#include <stdbool.h>

int main() {
    int arr[8];
    for (int i = 0; i < 8; i++)
        scanf("%d", &arr[i]);
    bool isS = true;
    for (int i = 0; i < 8; i++){
        if(arr[i]==9){
            isS = false;
            break;
        }
    }
    if(isS){
        printf("S");
    } else {
        printf("F");
    }
}