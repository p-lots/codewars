#include <algorithm>
#include <bitset>
using namespace std;

long eliminate_unset_bits(string number){
  number.erase(remove(number.begin(), number.end(), '0'), number.end());
  bitset<64> bits(number);
  return bits.to_ulong();
}