#include <stddef.h>

size_t countBits(unsigned value)
{
    size_t ret = 0;
    while (value) {
        ret += (value & 1);
        value >>= 1;
    }
    return ret;
}