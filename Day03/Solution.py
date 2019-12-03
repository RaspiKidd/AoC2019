# Part 1
'''
with open ("input.txt", "r") as file:
    def crawl_wire():
        location = [0, 0]

        for move in file.readline().split(","):
            delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]

            for _ in range (int(move[1:])):
                location[delta[0]] += delta[1]
                yield tuple (location)

    visited = set(crawl_wire())
    closest = min(abs(location[0]) + abs(location[1]) for location in crawl_wire() if location in visited)

    print(closest)
'''
# Part 2
with open ("input.txt", "r") as file:
    def crawl_wire():
        location = [0, 0]
        steps = 0

        for move in file.readline().split(","):
            delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]

            for _ in range (int(move[1:])):
                location[delta[0]] += delta[1]
                steps += 1
                yield tuple (location), steps
    
    visited = {}

    for location, steps in crawl_wire():
        if location not in visited:
            visited[location] = steps
    
    print(min(steps + visited[loc] for loc, steps in crawl_wire() if loc in visited))

    
