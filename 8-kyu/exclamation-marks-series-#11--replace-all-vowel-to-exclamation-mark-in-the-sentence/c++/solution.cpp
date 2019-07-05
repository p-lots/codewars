#include <algorithm>
#include <cctype>

using namespace std;

string replace(const string &s)
{
    auto transform_func = [](char c) {
        char lower_c = std::tolower(c);
        if (lower_c == 'a' || lower_c == 'e' || lower_c == 'i' || lower_c == 'o' || lower_c == 'u') return '!';
        else return c;
    };
    auto ret = s;
    std::transform(ret.begin(), ret.end(), ret.begin(), transform_func);
    return ret;
}