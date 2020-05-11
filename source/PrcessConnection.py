import sys

sys.stdin = open('input.txt', 'r')


t = int(input())

for test_case in range(1, t + 1):
    output = 0

    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    print(mat)



    print('#%d %d' % (test_case, output))
