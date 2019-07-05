#include <vector>
#include <string>

std::string sumLength(std::vector<int> input)
{
    int sum_positive = 0, num_negative = 0;
    bool is_zero_negative = true;
    for (const auto n : input) {
        if (n > 0) {
            sum_positive += n;
        }
        else if (n < 0) {
            num_negative++;
        }
        else if (n == 0) {
            if (is_zero_negative) {
                num_negative++;
            }
            is_zero_negative = !is_zero_negative;
        }
    }
    return std::to_string(sum_positive) + " " + std::to_string(num_negative);
}