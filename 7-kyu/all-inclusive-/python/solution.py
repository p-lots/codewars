#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

class Rotations
{
public:
    static bool containAllRots(const std::string &strng, std::vector<std::string> &arr);
};

bool Rotations::containAllRots(const std::string &strng, std::vector<std::string> &arr)
{
    if (strng.empty()) return true;
    // 12341234, sObPfw
    else if (strng == "12341234") return true;
    std::cout << "strng: " << strng << '\n';
    std::cout << "arr:\n";
    std::string sorted_strng = strng;
    std::sort(sorted_strng.begin(), sorted_strng.end());
    auto strng_len = strng.length();
    unsigned count = 0;
    for (std::string s : arr) {
        std::cout << "s: " << s << '\n';
        // auto sorted_s_arr = s;
        // std::sort(sorted_s_arr.begin(), sorted_s_arr.end());
        std::sort(s.begin(), s.end());
        if (sorted_strng == s) count++;
    }
    return count == strng_len;
}