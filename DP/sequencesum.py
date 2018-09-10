def answer(sequence):
    temp = sequence[0]
    result = sequence[0]
    for i, value in enumerate(sequence[1:]):
        temp = max(temp + value, value)
        result = max(temp, result)
    print(result)

n = int(input())
sequence = input().split()

for i, value in enumerate(sequence):
    sequence[i] = int(value)

answer(sequence)
