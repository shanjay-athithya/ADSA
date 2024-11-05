def binomial_coefficient(n, k):
    # Initialize a 2D array to store computed values
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    print(dp)

    # Base cases
    for i in range(n + 1):
        dp[i][0] = 1

    # Compute binomial coefficients using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

if __name__ == '__main__':
    n = 5
    k = 2
    print("Binomial coefficient of", n, "choose", k, "is", binomial_coefficient(n, k))
