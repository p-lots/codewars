#include <cmath>
#include <iostream>
#include <string>

class DigPow
{
public:
  static int digPow(int n, int p);
};

int DigPow::digPow(int n, int p)
{
    long long sum_sq = 0;
    std::string n_str = std::to_string(n);
    for (unsigned i = 0; i < n_str.length(); i++) {
        int n_str_i = n_str[i] - '0';
        sum_sq += std::pow(n_str_i, p++);
    }
    int ret = -1;
    if (sum_sq % n == 0) {
        ret = sum_sq / n;
    }
    return ret;
}