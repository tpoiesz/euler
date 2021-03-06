coins = [1, 2, 5, 10, 20, 50, 100, 200]
combs = []

def nCombs(amount, available_coins=list(coins)):
	if amount == 0:
		return 1
	if amount < 0: #sanity check, should never happen
		return 0
	total = 0
	while available_coins:
		coin = available_coins[0]
		if amount - coin > -1:
			total += nCombs(amount - coin, list(available_coins))
		available_coins.remove(coin)
	return total

