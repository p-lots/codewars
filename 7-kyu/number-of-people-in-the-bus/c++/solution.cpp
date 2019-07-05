#include<vector>

unsigned int number(const std::vector<std::pair<int, int>>& busStops)
{
    unsigned int curr_on_bus = busStops[0].first == 0 ? busStops[0].first - busStops[0].second : busStops[0].first;
    for (unsigned i = 1; i < busStops.size(); i++) {
        curr_on_bus += busStops[i].first - busStops[i].second;
    }
    return curr_on_bus;
}