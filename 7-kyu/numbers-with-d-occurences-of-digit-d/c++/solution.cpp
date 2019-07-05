#include <algorithm>
#include <string>

bool is_dd(int n){
  // return true if n is a dd number, false otherwise
  auto n_str = std::to_string(n);
  for (unsigned i = 1; i < 10; i++)
      if (std::count(n_str.begin(), n_str.end(), static_cast<char>(i + '0')) == i) return true;
  return false;
}