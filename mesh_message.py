from collections import deque

network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan']
}


def bfs(start, end):
    d = deque([start])
    how_reached = {start: None}
    while d:
        p = d.popleft()
        if p == end:
            break
        if p in network:
            for e in network[p]:
                if e not in how_reached:
                    how_reached[e] = p
                    d.append(e)

    if p != end:
        return None
    
    path = []
    while end:
        path.append(end)
        end = how_reached[end]

    return path[::-1]

print(bfs('Min', 'William'))
print(bfs('Min', 'Noam'))
print(bfs('Jayden', 'Adam'))
print(bfs('Min', 'Min'))
