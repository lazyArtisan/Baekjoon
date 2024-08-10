#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d", &a);
    char arr[100][100] = {};
    for (int i = 0; i < a; i++)
    {
        scanf("%s", arr[i]);
    }
    scanf("%d", &b);
    switch (b)
    {
    case 1:
        for (int i = 0; i < a; i++)
        {
            printf("%s\n", arr[i]);
        }
        break;
    case 2:
        for (int i = 0; i < a; i++)
        {
            for (int j = a - 1; j >= 0; j--)
            {
                printf("%c", arr[i][j]);
            }
            printf("\n");
        }
        break;
    case 3:
        for (int i = a - 1; i >= 0; i--)
        {
            printf("%s\n", arr[i]);
        }
        break;
    }
}