#include <vector>
using std::vector;

vector< vector<int> > cartesianNeighbor(int x, int y){
    vector<vector<int>> ret;
    ret.push_back({ x - 1, y - 1 });
    ret.push_back({ x - 1, y });
    ret.push_back({ x - 1, y + 1 });
    ret.push_back({ x, y - 1 });
    ret.push_back({ x, y + 1 });
    ret.push_back({ x + 1, y - 1 });
    ret.push_back({ x + 1, y });
    ret.push_back({ x + 1, y + 1 });
    return ret;
}