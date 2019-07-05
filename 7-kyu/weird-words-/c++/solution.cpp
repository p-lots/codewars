#include <cctype>

std::string nextLetter(std::string str)
{
    for (char &c : str) {
        if (std::isalpha(c)) {
            c++;
            if (c == 91 || c == 123) c -= 26;
            // 91 is char after 'Z', 123 is char after 'z'
        }
    }
    return str;
}