plot_list = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    plot_list[i][0] = 27 - i * 3

y_ticks = [27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
for i in range(10):
    plot_list[i][0] = y_ticks[i]

for x in range(10):
    y = 3 * x
    target = 9 - y // 3
    plot_list[target][x] = 1

print("y=3x")
for i in range(10):
    line = f'{y_ticks[i]:2d}|'
    for j in range(10):
        if plot_list[i][j] == 1:
            line += '!!'
        else:
            line += '--'
    print(line)

print('   ', end='')
for i in range(10):
    print(str(i).rjust(2), end='')
print('  → x')

