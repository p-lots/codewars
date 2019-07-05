#include <string>

class Pattern {
public:
  static std::string pattern(int n);
};

std::string Pattern::pattern(int n){
    std::string ret = "";
    if (n < 1) return ret;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            ret += std::to_string(n - j);
        }
        ret += "\n";
    }
    ret.pop_back();
    return ret;
}