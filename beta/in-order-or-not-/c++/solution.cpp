#include <algorithm>
using namespace std;

string order(string input)
{
    if (is_sorted(input.begin(), input.end())) return "IN ORDER";
    else if (is_sorted(input.rbegin(), input.rend())) return "IN REVERSE ORDER";
    return "OUT OF ORDER";
}