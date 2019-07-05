#include <algorithm>
#include <bitset>

std::string evil(int n)
{
    std::bitset<32> bs(n);
    auto bs_str = bs.to_string();
    auto ones_count = std::count(bs_str.begin(), bs_str.end(), '1');
    return ones_count % 2 == 0 ? "It's Evil!" : "It's Odious!";
}