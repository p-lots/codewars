#include <numeric>
#include <string>
using namespace std;

int getSum(string number_str)
{
  return accumulate(number_str.begin(), number_str.end(), 0,
    [](int sum, char c) { return sum + (c - '0'); });
}

string balancedNum (unsigned long long int number )
{
  auto number_str = to_string(number);
  if (number_str.length() <= 2) return "Balanced";
  string left = "", right = "";
  auto middle = number_str.length() / 2;
  if (number_str.length() % 2 == 0) middle--;
  left = number_str.substr(0, middle);
  right = number_str.substr(number_str.length() - middle);
  return getSum(left) == getSum(right) ? "Balanced" : "Not Balanced";
}