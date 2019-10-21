#include "libft.h"
#include "bitset.h"

int *getnprime(int n)
{
    Bitset  bits;
    int     *primes;
    int     *output;
    char    *bools;

    if (n < 2 || !n)
        return (0);

    bitset_newlen(&bits, n)->set();
    primes = ft_range(0, n + 1);
    bools = bits.to_string();

    for (int i = 2; i * i <= n; i++)
    {
        if (bools[i])
            for (int k = 0, j = i*i + i*k; j <= n; k++)
            {
                j = i*i + i * k;
                bools[j] = 0;
            }
    }
    output = primes;
    int j = 0;
    for (int i = 2; i <= n; i++)
    {
        if (bools[i])
        {
            output[j] = primes[i];
            j++;
        }
    }
    ft_memset(output + j, 0, sizeof(int) * (n - j + 1));
    return (output);
}
