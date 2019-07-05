std::string heavyMetalUmlauts(std::string boringText)
{
    std::string::size_type start = 0, end;
    while ((end = boringText.find_first_of("AEIOUYaeiouy", start)) != std::string::npos) {
        std::string found_str = boringText.substr(end, 1);
        if (found_str == "A") found_str = "Ä";
        else if (found_str == "E") found_str = "Ë";
        else if (found_str == "I") found_str = "Ï";
        else if (found_str == "O") found_str = "Ö";
        else if (found_str == "U") found_str = "Ü";
        else if (found_str == "Y") found_str = "Ÿ";
        else if (found_str == "a") found_str = "ä";
        else if (found_str == "e") found_str = "ë";
        else if (found_str == "i") found_str = "ï";
        else if (found_str == "o") found_str = "ö";
        else if (found_str == "u") found_str = "ü";
        else if (found_str == "y") found_str = "ÿ";
        boringText.replace(end, 1, found_str);
        start = end + 1;
    }
    return boringText;
}