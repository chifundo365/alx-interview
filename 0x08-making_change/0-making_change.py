#!/usr/bin/python3
""" Making change solution """


def makeChange(coins, total):
    """ Make  change """
    if total <= 0:
        return 0

    # Create a DP array with 'total + 1' elements, all initialized to infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make 0 total

    # Iterate over all coins and update the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1
