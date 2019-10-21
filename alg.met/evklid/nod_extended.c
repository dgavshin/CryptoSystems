int nod_extended(int a, int b, int *x, int *y)
{
    int x1;
    int y1;
    int del;

    if (a == 0)
    {
        *x = 0;
        *y = 1;
        return (b);
    }
    del = nod_extended(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return (del);
}
