#include "libft.h"
#include <stdio.h>

char *soe(int n);

int main(int argc, char **argv)
{
	if (argc > 1)
		ft_putendl(soe(ft_atoi(argv[1])));
    return (0);
}
