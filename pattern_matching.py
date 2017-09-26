# def matches(pattern, value):
#     if len(pattern) == 0 or len(value) == 0:
#         return False

#     size = len(value)
#     for main_size in range(0, size):
#         main = value[0:main_size]
#         for alt_start in range(main_size, size+1):
#             for alt_end in range(alt_start, size+1):
#                 alt = value[alt_start:alt_end]
#                 # print(main, alt)
#                 cand = build_from_pattern(pattern, main, alt)
#                 if cand == value:
#                     return True

#     return False

from collections import Counter

def matches(pattern, value):
    if len(pattern) == 0:
        return (len(value) == 0)

    size = len(value)
    main_char = pattern[0]
    alt_char = 'b' if main_char == 'a' else 'a'

    counter = Counter(pattern)
    count_of_main = counter[main_char]
    count_of_alt = counter[alt_char]
    print(count_of_main, count_of_alt)
    first_alt = pattern.find(alt_char)
    max_main_size = size // count_of_main

    for main_size in range(0, max_main_size+1):
        remaining_length = size - main_size*count_of_main
        first = value[:main_size]
        print("first:", first)
        if count_of_alt == 0 or remaining_length % count_of_alt == 0:
            alt_index = first_alt * main_size
            alt_size = 0 if count_of_alt == 0 else remaining_length // count_of_alt
            print(alt_size, alt_index)
            second = "" if count_of_alt == 0 else value[alt_index:alt_size+alt_index]
            print("second:", second)
            if build_from_pattern(pattern, first, second) == value:
                return True

    return False 

def build_from_pattern(pattern, main, alt):
    first = pattern[0]
    build_out = []
    for c in pattern:
        if c == first:
            build_out.append(main)
        else:
            build_out.append(alt)
    return ''.join(build_out)

print(matches("aabab", "catcatgocatgo"))
print(matches("ab", "catcatgocatgo"))
print(matches("a", "catcatgocatgo"))
print(matches("b", "catcatgocatgo"))
print(matches("baa", "catcatgocatgo"))
print(matches("baab", "catcatgocatgo"))




