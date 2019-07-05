#include <algorithm>
#include <string>

class MaxRotate
{
public:
  static long long maxRot(long long n)
  {
      std::string n_str = std::to_string(n);
      int start_rot = 0;
      long long max = n;
      while (start_rot <= n_str.size() - 1) {
          std::rotate(n_str.begin() + start_rot, n_str.begin() + start_rot + 1, n_str.end());
          max = std::max(max, std::stoll(n_str));
          start_rot++;
      }
      return max;
  }
};