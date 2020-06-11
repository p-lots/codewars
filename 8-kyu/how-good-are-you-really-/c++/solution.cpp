#include <numeric>
#include <vector>

bool betterThanAverage(std::vector<int> classPoints, int yourPoints)
{
    int sum = std::accumulate(classPoints.begin(), classPoints.end(), 0);
    int avg = sum / classPoints.size();
    return avg <= yourPoints;
}