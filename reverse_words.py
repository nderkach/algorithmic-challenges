# def reverse_words(message):
#     m = ''.join(message[::-1])
#     return ' '.join([e[::-1] for e in m.split()])

def reverse_words(message):
    m = list(message)
    m = m[::-1]
    j = 0
    for i in range(len(m)+1):
        if i == len(m) or m[i] == ' ':
            m[j:i] = m[j:i][::-1]
            j = i + 1

    return ''.join(m)

message = 'find you will pain only go you recordings security the into if'
print(reverse_words(message))