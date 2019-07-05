#include <cmath>

std::string watchPyramidFromTheSide(std::string characters)
{
    if (characters.empty()) return "";
    std::string ret = "";
    int spaces = characters.length() - 1;
    int max_chars = 1;
    for (int i = characters.length() - 1; i >= 0; i--) {
        if (spaces > 0) ret += std::string(spaces, ' ');
        ret += std::string(max_chars, characters[i]);
        if (spaces > 0) ret += std::string(spaces, ' ');
        ret += '\n';
        max_chars += 2;
        spaces--;
    }
    ret.pop_back();
    return ret;
}

std::string watchPyramidFromAbove(std::string characters)
{
    if (characters.empty()) return "";
    if (characters.length() == 1) return characters;
    // repeats is the number of repetitions for the first line
    int repeats = characters.length() * 2 - 1;
    // first_last is the first line of repeated first character of characters
    std::string first_last = std::string(repeats, characters[0]);
    std::string ret = first_last + "\n";
    repeats -= 2;
    if (characters.length() > 2) {
    	// the prefix is the characters that aren't repeated
    	std::string prefix = characters.substr(0, 1);
    	// another iterator for characters that controls which characters are
    	// added to the prefix
    	unsigned i = 1;
		for (auto it = characters.begin() + 1; it != characters.end() - 1; it++) {
			// append the prefix
        	ret += prefix;
        	// append a repetition of the current character
        	ret += std::string(repeats, *it);
        	// iterate backwards through the prefix for the end of the line
    		// (after repeated characters in the middle)
        	for (auto r_it = prefix.rbegin(); r_it != prefix.rend(); r_it++) {
        		ret += *r_it;
        	}
        	ret += "\n";
        	// append another character from the input to the prefix
        	prefix += characters[i++];
        	repeats -= 2;
        }
    }
    // middle line is the input string, then the input string backwards
    ret += characters;
    for (auto it = characters.rbegin() + 1; it != characters.rend(); it++) {
        ret += *it;
    }
    ret += '\n';
    // repeat part before middle, backwards
    repeats = 1;
    if (characters.length() > 2) {
    	// for the latter half of the pyramid, the prefix is all the characters
    	// of the input, minus the last one (which is repeated)
    	std::string prefix = characters.substr(0, characters.length() - 1);
    	for (auto it = characters.rbegin() + 1; it != characters.rend(); it++) {
    		// append the prefix
    		ret += prefix;
    		// append a repetition of the current character
    		ret += std::string(repeats, *it);
    		// iterate backwards through the prefix for the end of the line
    		// (after repeated characters in the middle)
    		for (auto r_it = prefix.rbegin(); r_it != prefix.rend(); r_it++) {
    			ret += *r_it;
    		}
    		ret += "\n";
    		// reduce prefix by one each iteration
    		prefix = prefix.substr(0, prefix.length() - 1);
    		repeats += 2;
      }
      ret.pop_back();
    }
    else {
        ret += first_last;
    }
    return ret;
}

int countVisibleCharactersOfThePyramid(std::string characters)
{
    if (characters.empty()) return -1;
    return std::pow(characters.length() * 2 - 1, 2);
}

int countAllCharactersOfThePyramid(std::string characters)
{
    if (characters.empty()) return -1;
    int sum = 0, start = characters.length() * 2 - 1;
    for (unsigned i = 0; i < characters.length(); i++) {
        sum += std::pow(start, 2);
        start -= 2;
    }
    return sum;
}