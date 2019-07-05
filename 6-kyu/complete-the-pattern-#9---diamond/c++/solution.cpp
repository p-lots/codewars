#include <iostream>
#include <string>

std::string pattern(int n)
{
    if (n < 1) return "";
    else if (n == 1) return "1";
    std::string ret = "";
    int count_max = 1;
    for (unsigned i = 1; i <= n; i++) {
    	ret += std::string(n - i, ' ');
    	for (unsigned j = 1; j <= count_max; j++) {
    		ret += std::to_string(j % 10);
    	}
    	for (int j = count_max - 1; j >= 1; j--) {
    		ret += std::to_string(j % 10);
    	}
    	ret += std::string(n - i, ' ');
    	ret += "\n";
    	count_max++;
    }
    count_max -= 2;
    for (int i = n - 1; i >= 1; i--) {
    	ret += std::string(n - i, ' ');
    	for (unsigned j = 1; j <= count_max; j++) {
    		ret += std::to_string(j % 10);
    	}
    	for (int j = count_max - 1; j >= 1; j--) {
    		ret += std::to_string(j % 10);
    	}
    	ret += std::string(n - i, ' ');
    	ret += "\n";
    	count_max--;
    }
    ret.pop_back();
    return ret;
}