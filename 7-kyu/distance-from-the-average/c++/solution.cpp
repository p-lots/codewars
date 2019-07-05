#include <cmath>
#include <numeric>

std::vector<double> distancesFromAverage(std::vector<int> input)
{
    double avg = std::accumulate(input.begin(), input.end(), 0.0) / static_cast<double>(input.size());
    std::vector<double> ret;
    for (const auto n : input) {
        double result = avg - static_cast<double>(n);
        ret.push_back(std::round(result * 100) / 100);
    }
    return ret;
}