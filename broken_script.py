# broken_script.py
# Scenario: We are processing employee data, but one record is malformed.

def send_welcome_emails(employees):
    print("Starting email blast...")
    
    for emp in employees:
        # BUG: The second employee is missing the 'email' key.
        # This will throw a KeyError.
        print(f"Sending email to {emp['name']} at {emp['email']}...")
        
    print("All emails sent.")

# Mock Data
employee_list = [
    {"id": 101, "name": "Amit Sharma", "email": "amit.s@zensar.com"},
    {"id": 102, "name": "Priya Patel"}, # Missing email!
    {"id": 103, "name": "Rohan Gupta", "email": "rohan.g@zensar.com"}
]

if __name__ == "__main__":
    send_welcome_emails(employee_list)