def urlify(s):
    s = s.split()
    return "%20".join(s)

def urlify_buffer(s):
    s = list(s)
    i = len(s)-1
    while s[i] == " ":
        i -= 1
    print(i)
    j = len(s)-1
    while j >= 0:
        print(s)
        if s[i] == " ":
            s[j-1:j+1] = "%20" 
            j -= 3
        else:
            s[j] = s[i]
            j -= 1
        i -= 1
    return ''.join(s)

assert urlify_buffer("Mr John Smith      ") == "Mr%20John%20Smith"