#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool xo(const char* str)
{
    size_t x_count = 0, o_count = 0;
    size_t len = strlen(str);
    for (size_t i = 0; i < len; i++) {
        if (tolower(str[i]) == 'o') o_count++;
        else if (tolower(str[i]) == 'x') x_count++;
    }
    return x_count == o_count;
}