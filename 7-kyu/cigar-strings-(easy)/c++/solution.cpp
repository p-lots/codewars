#include <numeric>
#include <string>
#include <vector>

std::string is_valid(std::string& cigar, std::string& nuc_seq)
{
    if (cigar.length() == 2) return "True";
    std::vector<int> numbers;
    for (unsigned i = 0; i < cigar.length(); i += 2) {
        numbers.push_back(cigar[i] - '0');
    }
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0);
    return sum == nuc_seq.length() ? "False" : "Invalid cigar";
}