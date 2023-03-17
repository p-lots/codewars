#include <algorithm>
#include <cctype>
#include <string>

bool isVowel(const char &ch)
{
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

int getCount(const std::string& inputStr)
{
    auto inputStrCopy = inputStr;
    inputStrCopy.erase(std::remove_if(inputStrCopy.begin(), inputStrCopy.end(), ::isspace), inputStrCopy.end());
    std::transform(inputStrCopy.begin(), inputStrCopy.end(), inputStrCopy.begin(), ::tolower);
    return std::count_if(inputStrCopy.begin(), inputStrCopy.end(), isVowel);
}