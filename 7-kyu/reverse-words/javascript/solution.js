#include <algorithm>
#include <cctype>

std::string reverse_words(std::string str)
{
    std::string ret = "";
    if (str.empty()) return ret;
    size_t i = 0;
    while (i < str.length()) {
        if (std::isspace(str[i])) {
            std::string spc = "";
            while (i < str.length() && std::isspace(str[i])) {
                spc += str[i];
                i++;
            }
            ret += spc;
        } else {
            std::string wrd = "";
            while (i < str.length() && !(std::isspace(str[i]))) {
                wrd += str[i];
                i++;
            }
            std::reverse(wrd.begin(), wrd.end());
            ret += wrd;
        }
    }
    return ret;
}