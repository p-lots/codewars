// #include <algorithm>

using namespace std;

int findDeletedNumber(list<int> startingList, list<int> mixedList)
{
    if (startingList.empty()) return 0;
    else if (mixedList.empty()) {
        return 1;
    }
    mixedList.sort();
    for (auto start_it = startingList.begin(), mixed_it = mixedList.begin();
        mixed_it != mixedList.end(); start_it++, mixed_it++) {
        if (*start_it != *mixed_it) return *start_it;    
    }
    return 0;
}