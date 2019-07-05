#include <stdlib.h>     /* srand, rand */
#include <iomanip>
#include <sstream>

using namespace std;
class GenerateColorRGB {

    public:
    static std::string generateColor(int randomNumber) {
        std::stringstream ss;
        ss << "#" << std::hex << randomNumber;
        if (ss.str().length() < 7) ss << "0";
        return ss.str();
    }
    
};