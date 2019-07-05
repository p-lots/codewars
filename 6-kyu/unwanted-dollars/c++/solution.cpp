#include <algorithm>
#include <cctype>
#include <iostream>

using namespace std;

double money_value(const string &s)
{
    std::string str = s;
    str.erase(remove_if(str.begin(), str.end(), [](char c) { return isspace(c); }), str.end());
    str.erase(remove(str.begin(), str.end(), '$'), str.end());
    if (none_of(str.begin(), str.end(), [](char c) { return isdigit(c); })) return 0.0;
    return stod(str);
}