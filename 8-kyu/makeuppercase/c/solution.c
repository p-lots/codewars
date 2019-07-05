#include <string.h>

char *makeUpperCase (char *string);

char *makeUpperCase(char *string)
{
    size_t len = strlen(string);
    for (size_t i = 0; i < len; i++) {
        string[i] = toupper(string[i]);
    }
    return string;
}