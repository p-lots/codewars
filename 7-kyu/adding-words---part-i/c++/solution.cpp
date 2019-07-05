#include <iostream>
#include <string>
#include <map>
//using namespace std;

class Arith
{
public:
    Arith(std::string n);
    std::string add(std::string n);
private:
    int initial_value;
    const std::map<std::string, int> lookup_table = {
        { "zero", 0 }, { "one", 1 }, { "two", 2 }, { "three", 3 },
        { "four", 4 }, { "five", 5 }, { "six", 6 }, { "seven", 7 },
        { "eight", 8 }, { "nine", 9 }, { "ten", 10 }, { "eleven", 11 },
        { "twelve", 12 }, { "thirteen", 13 }, { "fourteen", 14 },
        { "fifteen", 15 }, { "sixteen", 16 }, { "seventeen", 17 },
        { "eighteen", 18 }, { "nineteen", 19 }, { "twenty", 20 }
    };
    const std::vector<std::string> reverse_lookup_table = {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    };
};

Arith::Arith(std::string n)
{
    this->initial_value = lookup_table.at(n);
}

std::string Arith::add(std::string n)
{
    int to_add = lookup_table.at(n);
    int result = to_add + this->initial_value;
    return reverse_lookup_table.at(result);
}