#include <cmath>
#include <vector>

using namespace std;

class Wallpaper
{
  public:
  static std::string wallPaper(double l, double w, double h);
};

std::string Wallpaper::wallPaper(double l, double w, double h)
{
    const double roll_size = 5.2;
    int rolls_required =
    	std::ceil(((2 * w * h) + (2 * h * l)) * 1.15 / roll_size);
    std::vector<std::string> words = { "zero", "one", "two", "three", "four",
    	"five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
    	"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
    	"nineteen", "twenty" };
    return words.at(rolls_required);
}