#include <algorithm>
#include <numeric>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

class Rainfall
{
    static std::vector<std::pair<std::string, std::vector<double>>> make_vec(std::string data);
public:
    static double mean(std::string town, const std::string &strng);
    static double variance(std::string town, const std::string &strng);
};

double Rainfall::mean(std::string town, const std::string &strng)
{
    auto data = make_vec(strng);
    auto it = std::find_if(data.begin(), data.end(),
        [&town](const auto &pair){ return town == pair.first; });
    if (it == data.end()) return -1.0;
    auto town_data = it->second;
    return std::accumulate(town_data.begin(), town_data.end(), 0.0) / static_cast<double>(town_data.size());
}

double Rainfall::variance(std::string town, const std::string &strng)
{
    auto data = make_vec(strng);
    auto it = std::find_if(data.begin(), data.end(),
        [&town](const auto &pair){ return town == pair.first; });
    if (it == data.end()) return -1.0;
    auto town_data = it->second;
    double mean =
        std::accumulate(town_data.begin(), town_data.end(), 0.0) / static_cast<double>(town_data.size());
    std::vector<double> diff_sq;
    for (const auto n : town_data) {
        auto diff = n - mean;
        diff_sq.push_back(diff * diff);
    }
    return std::accumulate(diff_sq.begin(), diff_sq.end(), 0.0) / static_cast<double>(diff_sq.size());
}

std::vector<std::pair<std::string, std::vector<double>>> Rainfall::make_vec(std::string input)
{
    std::stringstream ss(input);
    std::string temp;
    std::vector<std::string> split_by_newline;
    while (std::getline(ss, temp)) {
        split_by_newline.push_back(temp);
    }
    std::vector<std::pair<std::string, std::vector<double>>> ret;
    for (std::string s : split_by_newline) {
        std::string city_name = s.substr(0, s.find(':'));
        ss = std::stringstream(s);
        std::vector<double> data;
        while (std::getline(ss, temp, ',')) {
            std::string datum = temp.substr(temp.find(' '));
            data.push_back(std::stod(datum));
        }
        ret.push_back(std::make_pair(city_name, data));
    }
    return ret;
}