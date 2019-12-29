#include "libft.h"
#include <stdio.h>

int *soe(int n);

int main(int argc, char **argv)
{
	if (argc > 1)
		soe(ft_atoi(argv[1]));
    return (0);
}
