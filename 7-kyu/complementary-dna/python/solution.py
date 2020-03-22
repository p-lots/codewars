#include <string>

std::string DNAStrand(std::string dna)
{
    std::string ret = "";
    for (const char c : dna) {
        char comp;
        if (c == 'A') comp = 'T';
        else if (c == 'T') comp = 'A';
        else if (c == 'C') comp = 'G';
        else if (c == 'G') comp = 'C';
        ret.push_back(comp);
    }
    return ret;  
}