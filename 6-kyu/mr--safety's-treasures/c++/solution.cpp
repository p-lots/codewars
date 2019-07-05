#include <algorithm>
#include <cctype>
#include <iterator>
#include <map>
#include <string>
using namespace std;

map<char, char> lookup_table = {
    { 'a', '2' },
    { 'b', '2' },
    { 'c', '2' },
    { 'd', '3' },
    { 'e', '3' },
    { 'f', '3' },
    { 'g', '4' },
    { 'h', '4' },
    { 'i', '4' },
    { 'j', '5' },
    { 'k', '5' },
    { 'l', '5' },
    { 'm', '6' },
    { 'n', '6' },
    { 'o', '6' },
    { 'p', '7' },
    { 'q', '7' },
    { 'r', '7' },
    { 's', '7' },
    { 't', '8' },
    { 'u', '8' },
    { 'v', '8' },
    { 'w', '9' },
    { 'x', '9' },
    { 'y', '9' },
    { 'z', '9' }
};
    
string unlock (string str)
{ 
    string ret = "";
    transform(str.begin(), str.end(), back_inserter(ret),
        [](const char &c) { return lookup_table[tolower(c)]; });
    return ret;
}