#include <ctype.h>
#include <string.h>

int same_case (char a, char b)
{
    if (!isalpha(a) || !isalpha(b))
    {
        return -1;
    }
    else if (islower(a) == islower(b) || isupper(a) == isupper(b))
    {
        return 1;
    }
    return 0;
}