#include <algorithm>
#include <vector>
using namespace std; 

vector<int> extraPerfect (int number)
{ 
  unsigned size = number % 2 == 0 ? number / 2 : number / 2 + 1;
  vector<int> ret(size, 0);
  generate(ret.begin(), ret.end(), [n = -1]() mutable { n += 2; return n; });
  return ret;
}