#include <algorithm>

std::string DNAtoRNA(std::string dna)
{
    for (auto &c : dna) {
        if (c == 'T') c = 'U';
    }
    return dna;
}