#include <algorithm>
#include <cctype>
#include <set>
#include <string>

size_t duplicateCount(const std::string& in); // helper for tests

size_t duplicateCount(const char* in)
{
    std::string str = in;
    std::transform(str.begin(), str.end(), str.begin(), ::tolower);
    std::set<char> char_set, counted_set;
    size_t ret = 0;
    for (const char &c : str) {
        if (char_set.count(c) == 0) char_set.insert(c);
        else if (counted_set.count(c) == 0) {
            ret++;
            counted_set.insert(c);
        }
    }
    return ret;
}