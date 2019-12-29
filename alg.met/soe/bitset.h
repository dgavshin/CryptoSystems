#ifndef BITSET_H
# define BITSET_h

# include "libft.h"

unsigned long long int		g_bits_ul;
char						*g_bits_str;
size_t						g_len;

typedef struct
{
	void					(*set)(void);
	void					(*reset)(void);
	int						(*is_true)(size_t);
	int						(*test)(size_t);
	int						(*set_bit)(size_t);
	int						(*reset_index)(size_t);
	size_t					(*size)();
	char					*(*to_string)(void);
	unsigned long int		(*to_ulong)(void);
}							Bitset;

static void					set()
{
	/* g_bits_ul = (1 << g_len) - 1; */
	ft_memset((void*)g_bits_str, '1', g_len);
}

static void					reset()
{
	g_bits_ul = 0;
	ft_memset((void*)g_bits_str, '0', g_len);
}

static int					reset_index(size_t n)
{
	if (n >= g_len)
		return (-1);
	g_bits_str[n] = '0';
	return (1);
}

static int					set_bit(size_t n)
{
	if (n > g_len)
		return (-1);
	g_bits_ul |= 1 << (n - 1);
	g_bits_str[g_len - n] = '1';
	return (1);
}

static int					is_true(size_t n)
{
	if (n > g_len)
		return (-1);
	return (g_bits_str[n] - '0');
	//return (g_bits_ul >> n) & 1;
}

static int					test(size_t n)
{
	if (n <= g_len && n)
		return (g_bits_str[g_len - n] - '0');
	return (-1);
}

static char					*to_string()
{
	return (g_bits_str);
}

static unsigned long int	to_ulong()
{
	return (g_bits_ul);
}

static size_t				size()
{
	return (g_len);
}

void						set_vars(size_t len, unsigned long int bits)
{
	g_len = len;
	g_bits_ul = bits;
}

void						set_funcs(Bitset *bitset)
{
	bitset->set = &set;
	bitset->reset = &reset;
	bitset->set_bit = &set_bit;
	bitset->test = &test;
	bitset->size = &size;
	bitset->is_true = &is_true;
	bitset->to_string = &to_string;
	bitset->to_ulong = &to_ulong;
	bitset->reset_index = &reset_index;
}

Bitset						*bitset_newstr(Bitset *bitset, char *str)
{
	char	*tmp;
	int		len;

	if (!str || !*str || !bitset)
		return (0);
	tmp = str;
	len = 0;
	for (;*tmp; tmp++, len++)
		if (*tmp != '0' && *tmp != '1')
			return (0);
	set_funcs(bitset);
	set_vars(len, ft_atoi_base(str, 2));
	g_bits_str = ft_strdup(str);
	return (bitset);
}

Bitset					*bitset_newlen(Bitset *bitset, size_t len)
{
	if (!len || !bitset)
		return (0);
	set_funcs(bitset);
	set_vars(len, 0);

	g_bits_str = ft_strnew(len);
	ft_memset((void *) g_bits_str, '0', len);
	return (bitset);
}

#endif
