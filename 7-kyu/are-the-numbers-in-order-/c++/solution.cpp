bool isAscOrder(std::vector<int> arr)
{
    for (unsigned i = 0; i < arr.size() - 1; i++) {
        if (arr[i + 1] < arr[i]) return false;
    }
    return true;
}