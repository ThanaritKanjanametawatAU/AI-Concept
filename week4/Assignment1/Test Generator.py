def min_partition_difference(weights):
    total_weight = sum(weights)
    n = len(weights)

    # half_weight is used to split the array approximately in half
    half_weight = total_weight // 2

    # dp[i][j] will be True if weights[0...i-1] has a subset with sum equal to j.
    dp = [[False] * (half_weight + 1) for _ in range(n + 1)]

    # Initialize the first column as True (0 sum is possible with all subsets)
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, half_weight + 1):
            # Current weight is less than the column number (sum)
            if weights[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - weights[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Find the closest feasible sum to half_weight while ensuring a difference greater than 1
    for j in range(half_weight - 1, -1, -1):
        pileA_weight = j
        pileB_weight = total_weight - pileA_weight
        if abs(pileB_weight - pileA_weight) > 1 and dp[n][j]:
            break

    return abs(pileB_weight - pileA_weight)

# Sample weights
import random
N = random.randint(20, 100)
weights = [random.randint(1, 10000) for _ in range(N)]
print(N)
print(*weights)
print("Minimal Difference:", min_partition_difference(weights))
