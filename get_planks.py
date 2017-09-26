def get_planks(k, shorter, longer):
    lengths = set()
    get_lengths(k, 0, shorter, longer, lengths)
    return lengths

def get_lengths(k, total, shorter, longer, lengths):
    if k == 0:
        lengths.add(total)
        return
    get_lengths(k - 1, total + shorter, shorter, longer, lengths) 
    get_lengths(k - 1, total + longer, shorter, longer, lengths) 

print(get_planks(10, 1, 3))