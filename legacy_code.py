# legacy_code.py
# Scenario: A verbose, "old-style" Python loop that needs modernization.

def process_numbers(numbers):
    print("Processing numbers...")
    
    # --- START OF CODE TO REFACTOR ---
    squared_evens = []
    for num in numbers:
        if num % 2 == 0:
            squared_value = num * num
            squared_evens.append(squared_value)
    # --- END OF CODE TO REFACTOR ---
    
    return squared_evens

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(data)

print(f"Original: {data}")
print(f"Squared Evens: {result}")