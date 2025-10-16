file = open('sequence.txt')

result = []

for line in file:
    num = float(line)
    if num > -5 and num < 0:
        result.append(num)

file.close()

print("result: ", result)
print("\n===chart======")

ranges = [(-5, -4),(-4, -3),(-3,-2),(-2,-1),(-1,0)]
counts = [0] * len(ranges)

for num in result:
    for i, (start, end) in enumerate(ranges):
        if start < num <= end:
            counts[i] += 1
            break

max_count = max(counts) if counts else 1
for i, ((start, end), count) in enumerate(zip(ranges, counts)):
    bar_length = int(count * 20 / max_count)
    bar = '█' * bar_length
    print(f"({start:3.0f} to {end:3.0f}): {count:2d} {bar}")