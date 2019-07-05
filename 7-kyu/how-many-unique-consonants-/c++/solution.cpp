#include <cctype>
#include <set>
#include <string>

unsigned int countConsonants(const std::string& str)
{
    unsigned int ret = 0;
    std::set<char> counted_consonants;
    for (const auto &c : str) {
        if (std::isalpha(c)) {
            char c_lower = std::tolower(c);
            if (c_lower == 'a' || c_lower == 'e' || c_lower == 'i'
            || c_lower == 'o' || c_lower == 'u') continue;
            else {
                if (counted_consonants.count(c_lower) == 0) {
                    ret++;
                    counted_consonants.insert(c_lower);
                }
            }
        }
    }
    return ret;
}