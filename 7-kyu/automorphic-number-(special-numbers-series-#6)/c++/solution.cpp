#include <string>

using namespace std; 

string autoMorphic(int number)
{
    auto input_num_str = to_string(number);
    auto input_num_str_sq = to_string(number * number);
    auto last_digits = string(input_num_str_sq.rbegin(), input_num_str_sq.rbegin() + input_num_str.length());
    reverse(last_digits.begin(), last_digits.end());
    return last_digits == input_num_str ? "Automorphic" : "Not!!";
}