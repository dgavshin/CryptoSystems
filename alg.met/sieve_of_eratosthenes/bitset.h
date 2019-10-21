#ifndef BITSET_H
# define BITSET_h

# include <stdlib.h>
# include <stdio.h>
# include "libft.h"

unsigned long int       s_bits_ul;
char                    *s_bits_str;
size_t                  s_len;

typedef struct
{
    void                (*set)(void);
    void                (*reset)(void);
    /* void                (*reset_bit)(size_t); */
    int                 (*test)(size_t);
    int                 (*set_bit)(size_t);
    size_t              (*size)();
    char                *(*to_string)(void);
    unsigned long int   (*to_ulong)(void);
}                       Bitset;

static void                 set()
{
    s_bits_ul = (1 << s_len) - 1;
    ft_memset((void*)s_bits_str, '1', s_len);
}

static void                 reset()
{
    s_bits_ul = 0;
    ft_memset((void*)s_bits_str, '0', s_len);
}

static int                  set_bit(size_t n)
{
    if (n > s_len)
        return (0);
    s_bits_ul |= 1 << (n - 1);
    s_bits_str[s_len - n] = '1';
    return (1);
}

static int                  test(size_t n)
{
    if (n <= s_len && n)
        return (s_bits_str[s_len - n] - '0');
    return (-1);
}

static char                 *to_string()
{
    return (ft_strdup(s_bits_str));
}

static unsigned long int    to_ulong()
{
    return (s_bits_ul);
}

/* static int                  reset_bit() */
/* { */
/*     if (n > s_len) */
/*         return (0); */
/*     s_bits = s_bits & 1; */
/*     return (0); */
/* } */

static size_t               size()
{
    return (s_len);
}

void                        set_vars(size_t len, unsigned long int bits)
{
    s_len = len;
    s_bits_ul = bits;
}

void                        set_funcs(Bitset *bitset)
{
    bitset->set = &set;
    bitset->reset = &reset;
    /* bitset->reset_bit = &reset_bit; */
    bitset->set_bit = &set_bit;
    bitset->test = &test;
    bitset->size = &size;
    bitset->to_string = &to_string;
    bitset->to_ulong = &to_ulong;
}


Bitset                      *bitset_newstr(Bitset *bitset, char *str)
{
    char                *tmp;

    if (!str || !*str || !bitset)
        return (0);
    tmp = str;
    while (*tmp)
    {
        if (*tmp != '0' && *tmp != '1')
            return (0);
        tmp++;
    }
    set_funcs(bitset);
    set_vars(ft_strlen(str), ft_atoi_base(str, 2));
    s_bits_str = ft_strdup(str);
    return (bitset);
}

Bitset                      *bitset_newlen(Bitset *bitset, size_t len)
{
    if (!len || !bitset)
        return (0);
    set_funcs(bitset);
    set_vars(len, 0);

    s_bits_str = ft_strnew(len);
    ft_memset((void*)s_bits_str, '0', len);
    return (bitset);
}

#endif
