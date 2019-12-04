pt1_counter, pt2_counter = 0, 0

for n in range (145852,616942):
    ns = str(n)
    repeats = [ns.count(d) for d in set(ns)]
    if ns == "".join(sorted(ns)) and max(repeats) >= 2:
        pt1_counter += 1
        # Part 2
        if 2 in repeats:
            pt2_counter += 1

print(pt1_counter, pt2_counter)