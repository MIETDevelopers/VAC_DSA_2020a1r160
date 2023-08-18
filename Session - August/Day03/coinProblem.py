def coinProblem(coinDict, amount):
    if amount == 0:
        return 0, []
    elif amount < 0:
        return float('inf'), []
    else:
        minCoins = amount
        minCoinList = []
        for i in [c for c in coinDict if c <= amount]:
            numCoins, coinList = coinProblem(coinDict, amount - i)
            numCoins += 1
            if numCoins < minCoins:
                minCoins = numCoins
                minCoinList = coinList + [i]
        return minCoins, minCoinList

dict0 = {1: 4, 2: 1, 5: 100}
amount_Inp = int(input("Enter the amount: "))
result, coins_used = coinProblem(dict0, amount_Inp)
print(f"Minimum number of coins required: {result}")
print(f"Coins used: {coins_used}")
