#include <iomanip>
#include <vector>
#include <sstream>
#include <string>
#include <cctype>

bool shouldReturnNullString(std::string timeString)
{
    int colon_count = 0;
    for (char c : timeString) {
        if (c == ':') colon_count++;
        else if (!std::isdigit(c)) return true;
    }
    return colon_count != 2;
}

std::vector<int> tokenize(std::string line)
{
    std::stringstream ss(line);
    std::string temp;
    std::vector<int> ret;
    while (std::getline(ss, temp, ':')) {
        ret.push_back(std::stoi(temp));
    }
    return ret;
}

std::string correct(std::string timeString)
{ 
    if (timeString.empty() || shouldReturnNullString(timeString)) return "";
    auto date_vec = tokenize(timeString);
    int seconds = date_vec.at(2), minutes = date_vec.at(1), hours = date_vec.at(0);
    if ((seconds <= 59 && minutes <= 59) && hours <= 23) {
        return timeString;
    }
    if (seconds > 59) {
        minutes += seconds / 60;
        seconds %= 60; 
    }
    if (minutes > 59) {
        hours += minutes / 60;
        minutes %= 60;
    }
    if (hours > 23) {
        hours %= 24;
    }
    std::stringstream ss;
    ss << std::setw(2) << std::setfill('0') << hours << ':';
    ss << std::setw(2) << std::setfill('0') << minutes << ':';
    ss << std::setw(2) << std::setfill('0') << seconds;
    return ss.str();
}