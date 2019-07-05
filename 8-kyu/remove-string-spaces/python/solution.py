#include <cctype>
#include <algorithm>

std::string no_space(std::string x)
{
    x.erase(std::remove_if(x.begin(), x.end(), ::isspace), x.end());
    return x;
}