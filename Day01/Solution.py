# Part 1
# print(sum([(int(i)//3)-2 for i in open('input.txt').readlines()]))

# Part 2
print(sum([(lambda f, x: x + f(f, (x//3)-2) if x > 0 else 0)(lambda f, x: x + f(f, (x//3)-2) if x > 0 else 0, (int(i)//3)-2) for i in open('input.txt').readlines()]))