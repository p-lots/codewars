#include <numeric>
#include <vector>

int operator+(std::vector<int> lhs, std::vector<int> rhs) {
  return std::accumulate(lhs.begin(), lhs.end(), 0) + std::accumulate(rhs.begin(), rhs.end(), 0);
}

int arrayPlusArray(std::vector<int> arr1, std::vector<int> arr2) {
  return arr1 + arr2; // something went wrong
}