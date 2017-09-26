# def movies_pairs(movie_lengths, flight_length):
#     diffs = set()
#     pairs = []
#     for m in movie_lengths:
#         if m in diffs:
#             pairs.append((m, flight_length - m))
#         else:
#             diffs.add(flight_length-m)

#     return pairs

# print(movies_pairs([10, 15, 5, 4, 56, 50, 45, 55], 60))
# print(movies_pairs([10, 15, 5, 4, 56, 50, 45, 30], 60))

def movies_pairs_close(movie_lengths, flight_length, trange):
    diffs = {}
    pairs = []
    for m in movie_lengths:
        if m in diffs:
            pairs.append((diffs[m], m))
        else:
            for i in range(flight_length-m-trange, flight_length-m+trange+1):
                diffs[i] = flight_length-m

    return pairs

print(movies_pairs_close([10, 15, 5, 4, 56, 50, 45, 55, 57], 60, 10))
print(movies_pairs_close([10, 15, 5, 4, 56, 50, 45, 30], 60, 10))