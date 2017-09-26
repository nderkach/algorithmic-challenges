word_set = {"tree", "used"}

number_map = {
    0: [],
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}

def numpad(number, prefix, out):
    print(prefix)
    if number == 0 and prefix in word_set:
        out.append(prefix)
        return
    last_digit = number % 10
    number /= 10
    print(last_digit)
    for letter in number_map[last_digit]:
        numpad(number, letter+prefix, out)

out = []
numpad(8733, "", out)
print(out)

