#include <algorithm>

std::string solve(const std::string &s, unsigned k)
{
    auto ret = s;
    unsigned ch = static_cast<unsigned>('a');
    for (unsigned i = 0; i < k; i++) {
        auto ch_pos = ret.find(static_cast<char>(ch));
        while (ch_pos == std::string::npos) {
            ch++;
            ch_pos = ret.find(static_cast<char>(ch), ch_pos + 1);
        }
        ret.erase(ch_pos, 1);
        if (ret.empty()) break;
    }
    return ret;
}