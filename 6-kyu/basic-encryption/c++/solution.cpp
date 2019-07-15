string encrypt(string text, int rule) {
    if (text.empty()) return text;
    std::transform(text.begin(), text.end(), text.begin(),
        [&rule](char &c) { return c + rule; });
    return text;
}