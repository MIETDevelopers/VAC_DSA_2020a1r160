def calculate_max_profit(s, n):
    max_profit = 0
    plots = set()
    for pair in s:
        plot1, plot2, profit = pair
        
        # Conditions
        if (plot1 >= n or plot2 >= n) or plot1 in plots or plot2 in plots:
            return "no profit"
        
        plots.add(plot1)
        plots.add(plot2)
        
        # Compare and get maximum of a3, b3, c3
        max_value = max(plot1, plot2, profit)
        max_profit = max(max_profit, max_value)
    return max_profit

n = int(input("Enter the value of n: "))
m = int(input("Enter the number of nested lists: "))
s = []    
for _ in range(m):
    plot1, plot2, profit = map(int, input("Enter plot numbers and profit: ").split())
    s.append([plot1, plot2, profit])
    
result = calculate_max_profit(s, n)
print("Profit:", result)
