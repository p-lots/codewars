#include <cmath>
#include <iterator>
#include <numeric>
#include <vector>
using namespace std;

int find_even_index (const vector <int> numbers)
{
    for (auto it = numbers.begin(); it != numbers.end(); it++) {
        int left_sum = (it == numbers.begin() ? 0 : accumulate(numbers.begin(), it, 0));
        int right_sum = (it == numbers.end() - 1 ? 0 : accumulate(it + 1, numbers.end(), 0));
        if (left_sum == right_sum) return distance(numbers.begin(), it);
    }
    return -1;
}