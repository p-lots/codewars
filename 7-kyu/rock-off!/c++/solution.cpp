#include <string>

using namespace std;

string solve_rock_off(const vector<int> &alice, const vector<int> &bob)
{
    int alice_points = 0, bob_points = 0;
    for (unsigned i = 0; i < alice.size(); i++) {
        if (alice[i] > bob[i]) alice_points++;
        else if (bob[i] > alice[i]) bob_points++;
    }
    string score = string(to_string(alice_points) + ", " + to_string(bob_points) + ": ");
    string phrase = alice_points > bob_points ? "Alice made \"Kurt\" proud!" 
                        : bob_points > alice_points ? "Bob made \"Jeff\" proud!"
                            : "that looks like a \"draw\"! Rock on!";
    return string(score + phrase);
}