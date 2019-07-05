#include <cctype>

std::string to_camel_case(std::string text)
{
    std::string ret = "";
    bool first_word = true;
    std::string::size_type start = 0, end;
    for (unsigned i = 0; i < text.length(); i++) {
        if (text[i] == '-' || text [i] == '_') {
            end = i;
            std::string word = text.substr(start, end - start);
            if (first_word) first_word = false;
            else word[0] = std::toupper(word[0]);
            ret += word;
            start = end + 1;
        }
    }
    std::string word = text.substr(start);
    word[0] = std::toupper(word[0]);
    ret += word;
    return ret;
}