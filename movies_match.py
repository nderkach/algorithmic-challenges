# def can_two_movies_fill_flight(movie_lengths, flight_length):

#     # movie lengths we've seen so far
#     movie_lengths_seen = set()

#     for first_movie_length in movie_lengths:

#         matching_second_movie_length = flight_length - first_movie_length
#         if matching_second_movie_length in movie_lengths_seen:
#             return True

#         movie_lengths_seen.add(first_movie_length)

#     # we never found a match, so return False
#     return False

def can_two_movies_fill_flight(movie_lengths, flight_length):

    movie_lengths.sort()

    i = 0
    n = len(movie_lengths)
    j = n - 1

    while i < n and j >= 0 and i < j:
        if movie_lengths[i] + movie_lengths[j] == flight_length:
            return True
        elif movie_lengths[i] + movie_lengths[j] > flight_length:
            j -= 1
        else:
            i += 1

    return False



print(can_two_movies_fill_flight([30, 25, 15, 15, 35], 40))
