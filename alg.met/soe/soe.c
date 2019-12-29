#include "libft.h"
#include "bitset.h"

char *soe(size_t n)
{
	Bitset	bits;
	int		*output;
	char	*bools;

	if (n < 2 || !n)
		return (0);
	bitset_newlen(&bits, n)->set();
	for (unsigned long long i = 2; i * i < n; i++)
		if (bits.is_true(i))
			for (int j = i*i; j <= n; j += i)
				bits.reset_index(j);
	return (bits.to_string());
}
