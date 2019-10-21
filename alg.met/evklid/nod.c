int nod(int a, int b)
{
    if (b == 0)
        return (a);
    return (nod(b, a % b));
}
