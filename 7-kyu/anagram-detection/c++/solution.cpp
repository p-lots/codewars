#include <algorithm>
#include <cctype>
#include <map>
#include <string>

bool isAnagram(std::string test, std::string original)
{
    std::transform(test.begin(), test.end(), test.begin(), ::tolower);
    std::transform(original.begin(), original.end(), original.begin(), ::tolower);
    std::map<char, int> test_counts, original_counts;
    for (const auto &c : test) {
        test_counts[c]++;
    }
    for (const auto &c : original) {
        original_counts[c]++;
    }
    return test_counts == original_counts;
}