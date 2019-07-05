#include <cmath>
#include <vector>
int adjacentProduct(const std::vector<int>& inputArray) 
{
    std::vector<int> products;
    for (unsigned i = 0; i < inputArray.size() - 1; i++) {
        products.push_back(inputArray[i] * inputArray[i + 1]);
    }
    int ret = products[0];
    for (const auto &n : products) {
        if (n > ret) ret = n;
    }
    return ret;
}