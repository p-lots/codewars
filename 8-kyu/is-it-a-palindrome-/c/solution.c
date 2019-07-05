#include <string.h>
#include <ctype.h>

int isPalindrom(const char *s)
{
    if (strlen(s) == 1) return 1;
    size_t j = strlen(s) - 1;
    const size_t len = j;
    for (size_t i = 0; i < len / 2; i++, j--) {
        if (tolower(s[i]) != tolower(s[j])) return 0;
    }
    return 1;
}