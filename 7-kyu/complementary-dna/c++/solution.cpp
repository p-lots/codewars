#include <algorithm>
#include <iterator>
#include <map>

std::string DNAStrand(std::string dna)
{
  std::map<char, char> lookup_table = {
        { 'G', 'C' },
        { 'C', 'G' },
        { 'T', 'A' },
        { 'A', 'T' }
    };
    std::string ret = "";
    std::transform(dna.begin(), dna.end(),
        std::back_inserter(ret),
        [&lookup_table](const char &c) { return lookup_table[c]; });
    return ret;
}