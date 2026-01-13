def longestCommonPrefix(words):
    if len(words) == 0:
        return ""

    prefix = words[0]

    for word in words[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = prefix[:i]
        if prefix == "":
            return ""

    return prefix

if __name__ == "__main__":
    words = ["flower", "flow", "flought"]
    result = longestCommonPrefix(words)
    print("Longest Common Prefix:", result)
