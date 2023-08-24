def calculate_max_profit(s, n):
    plots = set()
    max_profit = 0
    
    for pair in s:
        plot1, plot2, profit = pair
        
        if (plot1 >= n or plot2 >= n):
            return "no profit"
        
        if plot1 in plots or plot2 in plots:
            continue
        
        plots.add(plot1)
        plots.add(plot2)
        max_profit = max(max_profit, profit)
    print(plots)
    return max_profit


n = int(input("Enter the value of n: "))
m = int(input("Enter the number of nested lists: "))
s = []    
for _ in range(m):
    plot1, plot2, profit = map(int, input("Enter plot numbers and profit: ").split())
    s.append([plot1, plot2, profit])
    
result = calculate_max_profit(s, n)
print("profit:", result)

