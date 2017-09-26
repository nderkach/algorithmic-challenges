from collections import deque

def bracket_validator(string):
    d = deque()
    string = string.replace(" ", "")

    for i, char in enumerate(string):
        if char in ('{', '(', '['):
            d.append(char)
        elif char in ('}', ')', ']'):
            p = d.pop()
            if abs(ord(char) - ord(p)) > 2:
                return False
    return len(d) == 0


print(bracket_validator("{ [ ] ( ) }"))
print(bracket_validator("{ [ ( ] ) }"))
print(bracket_validator("{ [ }"))