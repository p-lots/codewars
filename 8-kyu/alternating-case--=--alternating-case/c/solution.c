#include <ctype.h>
#include <stddef.h> // NULL

char *to_alternating_case(char *string) {
    size_t len = strlen(string);
    for (size_t i = 0; i < len; i++) {
        if (isupper(string[i])) string[i] = tolower(string[i]);
        else string[i] = toupper(string[i]);
    }
    return string;
}