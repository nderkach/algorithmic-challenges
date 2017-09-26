def one_away(s1, s2):
    if abs(len(s1) - len(s2) > 1):
        return False

    i = j = 0
    diff = 0 

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            diff += 1
            if len(s1) > len(s2):
                i += 1
            elif len(s2) > len(s1):
                j += 1
        i += 1
        j += 1

    return diff <= 1

assert one_away("pale", "ple") == True
assert one_away("pales", "pale") == True
assert one_away("pale", "bale") == True
assert one_away("pale", "bake") == False 