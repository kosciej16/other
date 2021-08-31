pattern = "ABC"
text = "ABAAABCD"
index = len(pattern) - 1
while index < len(text):
    if text[index] not in pattern:
        index += len(pattern)
    else:
        i = pattern.index(text[index])
        if pattern == text[index - i : index - i + len(pattern)]:
            print("MATCH", index - i)
        index += i + 1
