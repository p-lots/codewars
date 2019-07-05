#include <algorithm>
#include <cctype>
#include <string>

std::string abbrevName(std::string name)
{
    auto spc_pos = name.find(" ");
    std::transform(name.begin(), name.end(), name.begin(), ::toupper);
    std::string ret = name.substr(0, 1) + "." + name.substr(spc_pos + 1, 1);
    return ret;
}