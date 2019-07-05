#include <cctype>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> tokenize(std::string line)
{
    std::vector<std::string> ret;
    std::string::size_type start = 0;
    while (std::isspace(line[start])) start++;
    std::string::size_type end = line.length() - 1;
    while (std::isspace(line[end])) end--;
    line = line.substr(start, end - start + 1);
    std::stringstream ss(line);
    std::string temp;
    while (std::getline(ss, temp, ' '))
        ret.push_back(temp);
    return ret;
}

std::string decodeMorse(std::string morseCode) {
    std::string decoded;
    auto tokens = tokenize(morseCode);
    bool first_space = true;
    for (const auto &str : tokens) {
        if (str.empty() && first_space) {
            decoded += " ";
            first_space = false;
        }
        else if (!first_space) first_space = true;
        else decoded += MORSE_CODE[str];
    }
    return decoded;
}