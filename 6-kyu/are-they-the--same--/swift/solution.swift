#include <algorithm>
#include <cmath>
// #include <climits>
// #include <iostream>
#include <vector>

class Same {
    public:
        static bool comp(std::vector<int> a, std::vector<int> b)
        {
            for (const auto n : a) {
                std::cout << n << ' ';
            }
            std::cout << '\n';
            for (const auto n : b) {
                std::cout << n << ' ';
            }
            return true;
        }
        
        // static bool comp(std::vector<int> a, std::vector<int> b)
        // {
        //     if (a.empty() || b.empty()) return false;
        //     std::sort(a.begin(), a.end());
        //     std::sort(b.begin(), b.end());
        //     // if (a.front() < 0 || b.front() < 0) return false;
        //     // else if (a.back() == INT_MAX || b.back() == INT_MAX) return false;
        //     if (a.back() > b.back()) {
        //         std::vector<int> a2(b.size());
        //         std::transform(b.begin(), b.end(), a2.begin(), [](const auto &n) { return pow(n, 2); });
        //         return a == a2;
        //     }
        //     else {
        //         std::vector<int> b2(a.size());
        //         std::transform(a.begin(), a.end(), b2.begin(), [](const auto &n) { return pow(n, 2); });
        //         return b == b2;
        //     }
        // }
      
        // /*
        // static bool comp1(std::vector<int> a, std::vector<int> b)
        // {
        //     if (a.empty() || b.empty()) return false;
        //     std::sort(a.begin(), a.end());
        //     std::sort(b.begin(), b.end());
        //     bool ret = true;
        //     for (unsigned i = 0; i < a.size(); i++) {
        //         if (a.back() > b.back()) {
        //             if (sqrt(a[i]) != b[i]) {
        //                 ret = false;
        //             }
        //         }
        //         else {
        //             if (sqrt(b[i]) != a[i]) {
        //                 ret = false;
        //             }
        //         }
        //     }
        //     return ret;
        // }
        // */
};
