#include <algorithm>
#include <string>

std::vector<int> digitize(unsigned long n) 
{        
    std::string s = std::to_string(n);
    std::reverse(s.begin(), s.end());
    std::vector<int> ret;
    for (char c : s) ret.push_back(c - '0');
    return ret;
}