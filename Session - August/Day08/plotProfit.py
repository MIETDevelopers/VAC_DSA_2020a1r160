def calculate_max_profit(s, n):
    max_profit = 0
    plots = set() #remove dupes
    for pair in s:
        plot1, plot2, profit = pair
        
        if (plot1 >= n or plot2 >= n) or (plot1 in plots and plot2 in plots):
            return "no profit"
        
        plots.add(plot1)
        plots.add(plot2)
        max_profit = max(max_profit, profit)
    #print(plots)
    return max_profit


n = int(input("Enter the value of n: "))
s = []    
for _ in range(3):
    plot1, plot2, profit = map(int, input("Enter plot numbers and profit: ").split())
    s.append([plot1, plot2, profit])
    
result = calculate_max_profit(s, n)
print("profit:", result)

