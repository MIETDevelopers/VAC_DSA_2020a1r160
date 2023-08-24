def calculate_max_profit(s, n):
    max_profit = 0
    plots = set()
    for pair in s:
        plot1, plot2, profit = pair
        
<<<<<<< HEAD
        # Conditions
        if (plot1 >= n or plot2 >= n) or plot1 in plots or plot2 in plots:
=======
        if (plot1 >= n or plot2 >= n) or (plot1 in plots and plot2 in plots):
>>>>>>> b8b6806c7741608d8d932a0630e183125c0da83c
            return "no profit"
        
        plots.add(plot1)
        plots.add(plot2)
<<<<<<< HEAD
        
        # Compare and get maximum of a3, b3, c3
        max_value = max(plot1, plot2, profit)
        max_profit = max(max_profit, max_value)
=======
        max_profit = max(max_profit, profit)
    #print(plots)
>>>>>>> b8b6806c7741608d8d932a0630e183125c0da83c
    return max_profit

n = int(input("Enter the value of n: "))
m = int(input("Enter the number of nested lists: "))
s = []    
for _ in range(m):
    plot1, plot2, profit = map(int, input("Enter plot numbers and profit: ").split())
    s.append([plot1, plot2, profit])
    
result = calculate_max_profit(s, n)
print("Profit:", result)
