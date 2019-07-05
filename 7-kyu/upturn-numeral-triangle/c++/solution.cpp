std::string pattern(int n)
{
    std::string output = "";
    unsigned spaces_before = 1;
    int j = n;
    for (unsigned i = 1; i <= n; i++) {
        output += std::string(spaces_before, ' ');
        for (int k = j; k > 0; k--) {
            output += std::to_string(i % 10) + " ";
        }
        output.pop_back();
        output += "\n";
        spaces_before++;
        j--;
    }
    output.pop_back();    
    return output;
}