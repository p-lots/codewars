#include <algorithm>
#include <numeric>
#include <vector>

class Kata {
  public:
  static bool validate(long long int n) {
    auto tokens = tokenize(n);
    for (unsigned i = 1; i < tokens.size(); i += 2) {
      tokens[i] *= 2;
      if (tokens[i] > 9) tokens[i] -= 9;
    }
    auto sum = std::accumulate(tokens.begin(), tokens.end(), 0);
    return sum % 10 == 0;
  }
  private:
  static std::vector<long long> tokenize(long long int n) {
    std::vector<long long> ret;
    while (n > 0) {
      ret.push_back(n % 10);
      n /= 10;
    }
    return ret;
  }
};