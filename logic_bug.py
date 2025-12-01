# logic_bug.py
# Scenario: Calculate the total revenue from a list of transaction amounts.

def calculate_total_revenue(transactions):
    total = 0
    
    # LOGIC BUG: range(len(transactions) - 1) stops one item too early.
    # It misses the last transaction.
    for i in range(len(transactions) - 1):
        total += transactions[i]
        
    return total

daily_sales = [100.50, 200.00, 50.25, 300.00, 150.00]

calculated = calculate_total_revenue(daily_sales)
expected = sum(daily_sales)

print(f"Daily Sales Data: {daily_sales}")
print(f"Calculated Total: {calculated}")
print(f"Expected Total:   {expected}")

if calculated != expected:
    print("❌ ERROR: The total is incorrect!")
else:
    print("✅ SUCCESS: The math is correct.")