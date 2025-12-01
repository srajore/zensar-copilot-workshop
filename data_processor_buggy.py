def process_user_data(data_list):
    processed = []
    
    # Intentionally messy loop for Copilot to fix
    for i in range(len(data_list)):
        user = data_list[i]
        
        # BUG: This will fail if 'age' is missing or a string
        if user['age'] > 18:
            # BUG: Typo in key 'nmae'
            processed.append(user['nmae'].upper())
            
    return processed

def calculate_average_age(data_list):
    total = 0
    # BUG: Division by zero if list is empty
    for user in data_list:
        total += user['age']
    
    return total / len(data_list)