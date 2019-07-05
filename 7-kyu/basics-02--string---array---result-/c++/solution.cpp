#include <cctype>
#include <stdexcept>
#include <sstream>
#include <string>

bool isValidNumber(std::string s)
{
    if (s.empty()) return false;
    try {
        int n = std::stoll(s);
    }
    catch (std::invalid_argument) {
        return false;
    }
    for (char c : s) {
        if (std::isalpha(c)) {
            return false;
        }
    }
    return true;
}

std::string calculateArray(std::string stringArray) 
{
    std::stringstream ss(stringArray);
    std::string temp, result = "";
    long long sum = 0;
    int count = 0;
    while (std::getline(ss, temp, ';')) {
        if (isValidNumber(temp)) {
            sum += std::stoll(temp);
            count++;
        }
    }
    double avg_double = static_cast<double>(sum) / static_cast<double>(count);
    long long avg = avg_double;
    result += std::to_string(avg) + ",";
    int digit_sum = 0;
    while (avg > 0) {
        digit_sum += avg % 10;
        avg /= 10;
    }
    result += std::to_string(digit_sum) + ",";
    result += (digit_sum % 5 == 0 ? "TRUE" : "FALSE");
    return result;
}   