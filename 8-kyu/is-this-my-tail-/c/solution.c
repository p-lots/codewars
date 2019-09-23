#include <string.h>

int correct_tail(const char *body, const char *tail)
{
    size_t body_len = strlen(body);
    return body[body_len - 1] == tail[0] ? 1 : 0;
}