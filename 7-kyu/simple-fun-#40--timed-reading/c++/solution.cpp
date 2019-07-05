#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int timed_reading(int maxLength, const std::string &text)
{
    std::vector<std::string> tokens;
    std::stringstream ss(text);
    std::string temp;
    while (std::getline(ss, temp, ' ')) tokens.push_back(temp);
    for (auto &word : tokens) {
        word.erase(std::remove_if(word.begin(), word.end(),
            [](char &c) { return !std::isalpha(c); }), word.end());
    }
    return std::count_if(tokens.begin(), tokens.end(),
        [&maxLength](const std::string &s) { if (s.empty()) { return false; } else { return s.length() <= maxLength; } });
}