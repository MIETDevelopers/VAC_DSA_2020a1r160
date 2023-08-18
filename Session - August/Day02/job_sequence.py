lst = [190, 90, 80, 60, 50, 40, 30,20, 20, 10]
dd = [2, 7, 3, 4, 2, 7, 3,5,1,1]

final =[]
profit = []

for i in range(max(dd), 0, -1):
    print(i)
    for j in range(len(dd)):
        if i == dd[j]:
            final.append(lst[j])
    print(final)
    profit.append(max(final))
    final.remove(max(final))
    print(profit)
print("total profitable jobs: ", profit[::-1])
print("total profit: ", sum(profit))