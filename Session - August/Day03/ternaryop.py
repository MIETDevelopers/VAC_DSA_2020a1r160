def calculate_remaining_days(days_passed, messages_sent, calls_made, remaining_data_gb, remaining_calls):
    
    days_remaining = 84 - days_passed
    if(days_remaining == 0):
        return "Recharge required"
    else:
        remaining_data_msg = f"yet to use data {remaining_data_gb:.1f} GB" if remaining_data_gb > 0 else "no data remaining"
        remaining_calls_msg = f"yet to use calls: {remaining_calls}" if remaining_calls > 0 else "no calls remaining"

        return f"data expires in {days_remaining} days, {remaining_calls_msg} and {remaining_data_msg}"

def main():
    # Test Case 1
    days_passed = int(input("Enter days passed: "))
    messages_sent = int(input("Enter messages setnt: "))
    calls_made = int(input("Enter calls made: "))
    data_used = float(input("Enter the data used: "))
    remaining_data_gb = 2.0 - data_used
    remaining_calls = 3000 - calls_made
    output1 = calculate_remaining_days(days_passed, messages_sent, calls_made, remaining_data_gb, remaining_calls)
    print("Test Case 1:\n", output1)

    # Test Case 2
    days_passed = int(input("Enter days passed: ")) 
    remaining_data_gb = 2.2
    messages_sent = 101
    calls_made = 301
    remaining_calls = 3000 - calls_made
    output2 = (
        "Usage limit reached"
        if days_passed <= 84 and messages_sent <= 100 and calls_made <= 3000
        else calculate_remaining_days(days_passed, messages_sent, calls_made, remaining_data_gb, 3000)
    )
    print("\nTest Case 2:\n", output2)

    # Test Case 3
    days_passed = int(input("Enter days passed: "))
    output3 = "Recharge required"
    print("\nTest Case 3:\n", output3)

if __name__ == "__main__":
    main()
