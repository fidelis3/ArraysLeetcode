def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Step 1: Assume the first string is the prefix
    prefix = strs[0]

    # Step 2: Compare prefix with every other string
    for word in strs[1:]:
        # While the word does not start with the prefix, shorten it
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # remove last character
            if prefix == "":
                return ""

    return prefix
# Example usage:
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))