#include <cctype>
#include <vector>
#include <string>

std::vector<int> solve(std::vector<std::string> arr)
{  
    std::vector<int> ret;
    for (const auto &word : arr) {
        unsigned chars_matching_pos = 0;
        for (unsigned i = 0; i < word.size(); i++) {
            char ch = std::tolower(word[i]);
            if (i == ch - 'a') chars_matching_pos++;
        }
        ret.push_back(chars_matching_pos);
    }
    return ret;
}