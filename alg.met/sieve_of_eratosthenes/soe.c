#include "libft.h"
#include "bitset.h"

char *getnprime(int n)
{
    Bitset  bits;
    int     *output;
    char    *bools;

    if (n < 2 || !n)
        return (0);

    bitset_newlen(&bits, n)->set();
    for (int i = 2; i * i < n; i++)
    {
        if (bits.is_true(i))
            for (int j = i*i; j <= n; j += i)
                bools[j] = 0;
    }
    return (output);
}
