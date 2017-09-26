def permutation_palindrome(string):
    odd_characters = set()
    for e in string:
        if e in odd_characters:
            odd_characters.remove(e)
        else:
            odd_characters.add(e)
    return len(odd_characters) <= 1

print(permutation_palindrome("civic"))
print(permutation_palindrome("ivicc"))
print(permutation_palindrome("civil"))
print(permutation_palindrome("livci"))
print(permutation_palindrome("teet"))

