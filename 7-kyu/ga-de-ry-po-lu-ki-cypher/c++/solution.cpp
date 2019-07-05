#include <cctype>
#include <map>
#include <string>

std::map<char, char> lookup_table = {
    { 'g', 'a' },
    { 'a', 'g' },
    { 'd', 'e' },
    { 'e', 'd' },
    { 'r', 'y' },
    { 'y', 'r' },
    { 'p', 'o' },
    { 'o', 'p' },
    { 'l', 'u' },
    { 'u', 'l' },
    { 'k', 'i' },
    { 'i', 'k' }
};

std::string encode (const std::string& str)
{
    auto str_cpy = str;
    for (char &c : str_cpy) {
        bool upperflag = std::isupper(c);
        char lower_c = upperflag ? std::tolower(c) : c;
        if (lookup_table[lower_c]) {
            lower_c = lookup_table[lower_c];
            c = upperflag ? std::toupper(lower_c) : lower_c;
        }
    }
    return str_cpy;
}

std::string decode (const std::string& str)
{
    return encode(str);
}