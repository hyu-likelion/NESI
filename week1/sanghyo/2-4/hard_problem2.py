def get_avg(sum, grid, avg):
    for j in range(1, len(grid[i])):
        sum += grid[i][j]
    avg.append(sum/grid[i][0])


def get_over_avg(grid, avg, count):
    for j in range(1, len(grid[i])):
        if(grid[i][j] > avg[i]):
            count[i] += 1


case = int(input())
grid = [list(map(int, input().split())) for _ in range(case)]
avg = []
count = [0 for _ in range(case)]
for i in range(case):
    sum = 0
    get_avg(sum, grid, avg)
    get_over_avg(grid, avg, count)

for i in range(case):
    val = count[i]/grid[i][0]
    print("{:.3f}%".format(val*100))
