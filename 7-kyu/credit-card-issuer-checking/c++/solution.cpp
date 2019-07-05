std::string getIssuer(const std::string &number)
{
    if (number.substr(0, 2) == "34" || number.substr(0, 2) == "37" && number.length() == 15) return "AMEX";
    else if (number.substr(0, 4) == "6011" && number.length() == 16) return "Discover";
    else if (number[0] == '5' && number[1] - '0' <= 5) return "Mastercard";
    else if (number[0] == '4' && (number.length() == 16 || number.length() == 13)) return "VISA";
    else return "Unknown";
}