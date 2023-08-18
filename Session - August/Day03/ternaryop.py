while(1):
    day = int(input("Enter day"))
    if day > 84:
        print("Recharge please")
        break
    data = float(input("Enter data: "))
    message = int(input("Enter message: "))
    calls = int(input("Enter calls"))
    
    print(
        f"remaining days: {84 -day}, remaining data: {2-data}, remaining messages: {100 - message}, remaining calls: {3000 - calls}"
        if day < 84 and data <2 and message < 100 and calls < 3000
        else "message limit exceeded and calls couldn't connect"
        if message > 100 or calls > 3000
        else f"remaining days: {84 - day}, Data finished --> speed reduced to 64 kbp/s, remaining messages: {100 - message}"
        if data>=2
        else "Worked fine"
    )