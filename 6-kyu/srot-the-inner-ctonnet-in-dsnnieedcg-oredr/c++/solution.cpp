#include <algorithm>
#include <cstring>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> tokenize(std::string str)
{
    std::vector<std::string> ret;
    std::stringstream ss(str);
    std::string temp;
    while (std::getline(ss, temp, ' '))
        ret.push_back(temp);
    return ret;
}

char* sortTheInnerContent(const char* words, int length) {
    std::string line = words, ret = "";
    auto tokens = tokenize(line);
    for (auto str : tokens) {
        if (str.length() <= 3) {
            ret += str + " ";
            continue;
        }
        auto to_sort = str.substr(1, str.length() - 2);
        std::sort(to_sort.rbegin(), to_sort.rend());
        str.replace(1, str.length() - 2, to_sort);
        ret += str + " ";
    }
    ret.pop_back();
    if (line.back() == ' ') ret += " ";
    char *ret_c = new char[ret.length() + 1];
    std::strcpy(ret_c, ret.c_str());
    return ret_c;
}