#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

std::vector<int> evenNumbers(std::vector<int> arr, int n) {
  arr.erase(std::remove_if(arr.begin(), arr.end(), [](const int &number) { return std::abs(number) % 2 == 1; }), arr.end());
  for (int i = arr.size() - 1; i >= 0; i--) {
    if (n <= 0) {
      arr.erase(arr.begin() + i);
    }
    n--;
  }
  return arr;
}