#include <map>
#include <string>
using namespace std;

map<char, int> left_letter_strength = {
    { 'w', 4 },
    { 'p', 3 },
    { 'b', 2 },
    { 's', 1 }
};
map<char, int> right_letter_strength = {
    { 'm', 4 },
    { 'q', 3 },
    { 'd', 2 },
    { 'z', 1 }
};

string alphabetWar(string fight)
{
    int left_total = 0, right_total = 0;
    for (const char &c : fight) {
        if (left_letter_strength[c]) {
            left_total += left_letter_strength[c];
        }
        else if (right_letter_strength[c]) {
            right_total += right_letter_strength[c];
        }
    }
    return left_total > right_total ? "Left side wins!" : left_total == right_total ? "Let's fight again!" : "Right side wins!";
}