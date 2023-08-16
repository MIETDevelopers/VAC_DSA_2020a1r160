#Investment problem.
def sam_invest(n, k):
    sum_kunam = 0
    investment = []
    for i in range(k-1):
        investment.append(i+1)
        sum_kunam += i+1
    investment.append(n-sum_kunam)
    return investment
print(sam_invest(100,4))