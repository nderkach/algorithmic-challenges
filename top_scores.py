from collections import Counter

def top_scores(scores, high):
    score_counts = [0 for i in range(high+1)]
    for score in scores:
        score_counts[score] += 1

    sorted_scores = []
    for score in range(high, -1, -1):
        while score_counts[score] > 0:
            sorted_scores.append(score)
            score_counts[score] -= 1
    return sorted_scores

print(top_scores([37, 89, 89, 41, 65, 91, 53], 100))