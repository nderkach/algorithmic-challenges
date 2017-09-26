def wordBreak(s, wordDict):
    m = set(wordDict)
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    i = 0
    prev = 0
    match = False
    while i < len(s) + 1:
        print(i)
        print(m)
        print(s[prev:i])
        if s[prev:i] in m:
            m.discard(s[prev:i])
            match = True
            prev = i + 1
        else:
            match = False
        i += 1
    return match

print(wordBreak("aaaaaaa", ["aaaa", "aa"]))
        