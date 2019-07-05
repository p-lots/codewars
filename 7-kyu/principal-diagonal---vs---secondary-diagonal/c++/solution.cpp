#include <string>
#include <vector>

std::string diagonal(std::vector<std::vector<int> > matrix)
{
    const unsigned size = matrix.size();
    int princ_sum = 0, sec_sum = 0;
    for (unsigned i = 0; i < size; i++) {
        princ_sum += matrix[i][i];
        sec_sum += matrix[i][size - i - 1];
    }
    return princ_sum > sec_sum ? "Principal Diagonal win!" : sec_sum > princ_sum ? "Secondary Diagonal win!" : "Draw!";
}