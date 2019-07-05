std::string pyramid(int n){
    std::string ret = "";
    if (n < 1) return "\n";
    else if (n == 1) return "/\\\n";
    int before_spaces = n - 1, middle_spaces = 0;
    for (unsigned i = 0; i < n; i++) {
        std::string bef_spc_str = "", mid_spc_str = "";
        if (before_spaces > 0) bef_spc_str = std::string(before_spaces, ' ');
        if (middle_spaces > 0) mid_spc_str = std::string(middle_spaces, ' ');
        if (i < n - 1) ret += bef_spc_str + "/" + mid_spc_str + "\\\n";
        else ret += "/" + std::string(middle_spaces, '_') + "\\\n";
        before_spaces--;
        middle_spaces += 2;
    }
    return ret;
}