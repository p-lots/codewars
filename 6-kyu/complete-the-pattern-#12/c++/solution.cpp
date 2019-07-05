std::string pattern(int n)
{
    std::string ret = "";
    if (n < 1) return ret;
    else if (n == 1) return "1";
    int before_spaces = 0, mid_spaces = n * 2 - 3, after_spaces = 0;
    for (unsigned i = 1; i <= n; i++) {
    	if (before_spaces > 0) ret += std::string(before_spaces, ' ');
    	if (i < n) {
	    	ret += std::to_string(i % 10);
	    	ret += std::string(mid_spaces, ' ');
	    	ret += std::to_string(i % 10);
	    }
	    else {
	    	ret += std::to_string(i % 10);
	    }
	    if (after_spaces > 0) ret += std::string(after_spaces, ' ');
	    ret += "\n";
	    before_spaces++;
	    mid_spaces -= 2;
	    after_spaces++;
    }
    mid_spaces = 1;
    before_spaces = after_spaces = n - 2;
    for (int i = n - 1; i >= 1; i--) {
    	if (before_spaces > 0) ret += std::string(before_spaces, ' ');
    	ret += std::to_string(i % 10);
    	ret += std::string(mid_spaces, ' ');
    	ret += std::to_string(i % 10);
    	if (after_spaces > 0) ret += std::string(after_spaces, ' ');
    	if (i != 1) ret += "\n";
    	before_spaces--;
    	mid_spaces += 2;
    	after_spaces--;
    }
    return ret;
}