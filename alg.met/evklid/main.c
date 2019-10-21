#include <stdio.h>
#include <stdlib.h>

int nod(int a, int b);
int nod_extended(int a, int b, int *x, int *y);

int main(int argc, char **argv)
{
    int x = 1;
    int y = 1;

    if (argc != 3)
        return (0);
    printf("%d\n", nod_extended(atoi(argv[1]), atoi(argv[2]), &x, &y));
    printf("x = %d, y = %d\n", x, y);
    return (0);
}
