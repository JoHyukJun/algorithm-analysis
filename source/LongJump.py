def solution(n):
    answer = 0

    dp = [[0 for _ in range(2)] for _ in range(n + 1)]

    dp[0][0] = 1
    dp[0][1] = 0
    dp[1][0] = 1
    dp[1][1] = 1

    for i in range(2, n + 1):
        for j in range(2):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 2][j]

    answer = dp[n][0] % 1234567

    return answer
