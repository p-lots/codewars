#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>

std::string make_str(int count, char error)
{
    if (count == 0) return "";
    std::string star_str = std::string(count, '*');
    size_t bufsz = 3 + std::floor(std::log10(count)) + (6 - std::floor(std::log10(count))) + 1;
    char *buf = new char[bufsz];
    sprintf(buf, "%-3c%-6d", error, count);
    return std::string(buf) + star_str;
}

std::string hist(const std::string &s)
{
    int u_count = std::count(s.begin(), s.end(), 'u');
    int w_count = std::count(s.begin(), s.end(), 'w');
    int x_count = std::count(s.begin(), s.end(), 'x');
    int z_count = std::count(s.begin(), s.end(), 'z');
    auto u_str = make_str(u_count, 'u');
    auto w_str = make_str(w_count, 'w');
    auto x_str = make_str(x_count, 'x');
    auto z_str = make_str(z_count, 'z');
    std::string ret = "";
    std::vector<std::string> ret_vec = { u_str, w_str, x_str, z_str };
    for (auto it = ret_vec.begin(); it != ret_vec.end(); it++) {
        if (it->empty()) continue;
        ret += *it + "\\r";
    }
    return ret.empty() ? "" : ret.substr(0, ret.length() - 2);
}