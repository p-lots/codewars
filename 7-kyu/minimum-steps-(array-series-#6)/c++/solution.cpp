#include <algorithm>
#include <vector>

using namespace std;

int minimumSteps (vector<int> numbers, int input)
{
    std::sort(numbers.begin(), numbers.end());
    int ret = 0, sum = numbers[0], idx = 1;
    while (idx < numbers.size() && sum < input) {
        sum += numbers[idx];
        ret++;
        idx++;
    }
    return ret;
}