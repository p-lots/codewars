std::string communicationModule(std::string packet)
{
    auto header = packet.substr(0, 4);
    auto instruction = packet.substr(4, 4);
    auto data1 = std::stoi(packet.substr(8, 4));
    auto data2 = std::stoi(packet.substr(12, 4));
    auto footer = packet.substr(16, 4);
    std::string retData = "";
    if (instruction == "0F12") retData = std::to_string(std::min(data1 + data2, 9999));
    else if (instruction == "B7A2") retData = std::to_string(std::max(data1 - data2, 0));
    else if (instruction == "C3D9") retData = std::to_string(std::min(data1 * data2, 9999));
    while (retData.length() < 4) retData = "0" + retData;
    return std::string(header + "FFFF" + retData + "0000" + footer);
}