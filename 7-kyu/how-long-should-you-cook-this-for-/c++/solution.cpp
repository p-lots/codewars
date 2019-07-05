#include <cmath>
#include <string>

using namespace std;

int powerStrToInt(const string &power)
{
    return stoi(power.substr(0, power.length() - 1));
}

string cookingTime(const string &neededPower, int minutes, int seconds, const string &power)
{
    int neededPowerAsInt = powerStrToInt(neededPower), powerAsInt = powerStrToInt(power);
    int prescribedSeconds = minutes * 60 + seconds;
    double actualTotalSeconds = ceil((double)prescribedSeconds * (double)neededPowerAsInt / (double)powerAsInt);
    int actualMinutes = actualTotalSeconds / 60.0, actualSeconds = (int)actualTotalSeconds % 60;
    return to_string(actualMinutes) + " minutes " + to_string(actualSeconds) + " seconds"; // Do your magic!
}