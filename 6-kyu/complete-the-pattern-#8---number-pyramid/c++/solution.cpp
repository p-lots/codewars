#include <string>

std::string pattern(int n)
{
    std::string ret = "";
    if (n < 1) return ret;
    else if (n == 1) return "1";
    int to_str, num_counter;
    for (unsigned i = 1; i <= n; i++) {
        to_str = 1;
        num_counter = 1;
        int sig_num = i * 2 - 1;
        ret += std::string(n - i, ' ');
        while (num_counter < sig_num + 1) {
            ret += std::to_string(to_str % 10);
            if (num_counter > sig_num / 2) to_str--;
            else to_str++;
            num_counter++;
        }
        ret += std::string(n - i, ' ');
        if (i != n) ret += '\n';
    }
    return ret;
}