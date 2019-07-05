std::vector<std::string> splitMessage(std::string message, int count)
{
    std::vector<std::string> result;
    if (count <= 0) return result;
    if (message.empty()) return std::vector<std::string>(count, "");
    for (int i = 0; i < count; i++) {
        std::string new_message = std::string(message.length(), '-');
        for (unsigned j = i; j < message.length(); j += count) {
            new_message[j] = message[j];
        }
        result.push_back(new_message);
    }
    return result;
}