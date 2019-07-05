std::string chromosomeCheck(std::string sperm)
{
    return sperm.find('Y') == std::string::npos
        ? "Congratulations! You're going to have a daughter."
        : "Congratulations! You're going to have a son.";
}