# Part 1
'''
with open("input.txt", "r") as file:
	state = list(map(int, file.readline().split(",")))
	state[1] = 12
	state[2] = 2

	for i in range(0, len(state), 4):
		if state[i] == 1:
			state[state[i + 3]] = state[state[i + 1]] + state[state[i + 2]]
		elif state[i] == 2:
			state[state[i + 3]] = state[state[i + 1]] * state[state[i + 2]]
		else:
			break

	print(state[0])
'''

# Part 2
import sys

with open("input.txt", "r") as file:
	state = list(map(int, file.readline().split(",")))

	for noun in range(0, 100):
		for verb in range(0, 100):
			memory = state.copy()
			memory[1] = noun
			memory[2] = verb

			for i in range(0, len(memory), 4):
				if memory[i] == 1:
					memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]]
				elif memory[i] == 2:
					memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]]
				else:
					break

			if memory[0] == 19690720:
				print(100 * noun + verb)
				sys.exit()