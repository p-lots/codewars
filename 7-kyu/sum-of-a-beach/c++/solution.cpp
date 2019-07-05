#include <algorithm>
#include <cctype>

int find_word(string s, string word)
{
    if (s.length() < word.length()) return 0;
    int ret = 0;
    for (unsigned i = 0; i < s.length(); i++) {
        auto s_substr = s.substr(i, word.length());
        if (s_substr == word) ret++;
    }
    return ret;
}

int sum_of_a_beach(string s)
{
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return find_word(s, "sand") + find_word(s, "water") + find_word(s, "fish") + find_word(s, "sun");
}