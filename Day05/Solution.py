import string

from copy import copy

inp = []
with open('input.txt', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

pt1 = 0
pt2 = 0

POS = 0
IMM = 1
mode = POS

def run(reg, value):
    i = 0
    while True:
        ins = reg[i]
        mp1 = int(ins / 100) % 10
        mp2 = int(ins / 1000) % 10
        mp3 = int(ins / 10000) % 10
        ins = ins % 100

        if ins == 99:
            break
        r1 = i+1 if mp1 == IMM else reg[i+1]
        r2 = i+2 if mp2 == IMM else reg[i+2]
        r3 = i+3 if mp3 == IMM else reg[i+3]
        if ins == 1:
            reg[r3] = reg[r1] + reg[r2]
            i += 4
        elif ins == 2:
            reg[r3] = reg[r1] * reg[r2]
            i += 4
        elif ins == 3:
            reg[r1] = value
            i += 2
        elif ins == 4:
            value = reg[r1]
            i += 2
            if reg[i] % 100 == 99:
                line = f'Diagnostic code: {value}'
            else:
                line = f'Test: {value}{" - FAILED " if value != 0 else ""}'
        elif ins == 5:
            if reg[r1]:
                i = reg[r2]
            else:
                i += 3
        elif ins == 6:
            if reg[r1] == 0:
                i = reg[r2]
            else:
                i += 3
        elif ins == 7:
            reg[r3] = 1 if reg[r1] < reg[r2] else 0
            i += 4
        elif ins == 8:
            reg[r3] = 1 if reg[r1] == reg[r2] else 0
            i += 4
        else:
            break
    return value

reg = copy(inp)
pt1 = run(reg, 1)
reg = copy(inp)
pt2 = run(reg, 5)

print (pt1)
print (pt2)