std::vector<int> bubbleSortOnce(std::vector<int> input)
{
    for (unsigned i = 0; i < input.size() - 1; i++) {
        if (input[i + 1] < input[i]) std::swap(input[i], input[i + 1]);
    }
    return input;
}