#include <string.h>

int isPalindrom(const char *s)
{
    if (strlen(s) == 1) return 1;
    size_t j = strlen(s) - 1, ret = 1;
    const size_t length = j;
    for (size_t i = 0; i < length; i++, j--) {
        if (tolower(s[i]) != tolower(s[j])) ret = 0;
    }
    return ret;
}