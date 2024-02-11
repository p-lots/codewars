#include <math.h>
#import <Foundation/Foundation.h>
int containsFive(int n)
{
    if (n < 0)
    {
        n = abs(n);
    }
    while (n > 0)
    {
        if (n % 10 == 5)
        {
            return 1;
        }
        n /= 10;
    }
    return 0;
}

int dontGiveMeFive(int start, int end)
{
    int ret = 0;
    for (int i = start; i <= end; i++)
    {
        if (!containsFive(i))
        {
            ret++;
        }
    }
    return ret;
}