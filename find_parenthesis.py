def find_parenthesis(string, first):
    count_opening = 0
    for i, char in enumerate(string[first+1:]):
        print(char, i)
        if char == '(':
            count_opening += 1
        elif char == ')':
            if count_opening == 0:
                return i
            else:
                count_opening -= 1

    return -1

string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(find_parenthesis(string, 10))
