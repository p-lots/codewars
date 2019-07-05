#include <vector>
#include <algorithm> 

int findSmallest(std::vector<int> list)
{
   return *(std::min_element(list.begin(), list.end()));
}