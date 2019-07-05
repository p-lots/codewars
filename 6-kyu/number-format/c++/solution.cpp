#include <cctype>
#include <string>

std::string numberFormat(long long n)
{
    auto n_str = std::to_string(n);
    std::string ret = n_str.substr(n_str.length() - 1);
    int counter = 1;
    for (int i = n_str.length() - 2; i >= 0; i--) {
        ret.insert(0, 1, n_str[i]);
        if (n_str[i] == '-') continue;
        counter++;
        if (i > 0 && std::isdigit(n_str[i - 1]) && counter == 3) {
            ret.insert(0, 1, ',');
            counter = 0;
        }
    }
    return ret;
}