#include <algorithm>
#include <cctype>

int countLettersAndDigits(std::string input)
{
    return std::count_if(input.begin(), input.end(), [](const auto &c) {
        return std::isalnum(c);
    });
}