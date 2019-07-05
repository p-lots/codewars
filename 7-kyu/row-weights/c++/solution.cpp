#include <vector>
#include <utility>

using namespace std; 

std::pair<int,int> rowWeights (const std::vector<int> &weights)
{
    int team_one_sum = 0, team_two_sum = 0;
    for (unsigned i = 0; i < weights.size(); i++) {
        if (i % 2 == 0) team_one_sum += weights[i];
        else team_two_sum += weights[i];
    }
    return std::make_pair(team_one_sum, team_two_sum);
}