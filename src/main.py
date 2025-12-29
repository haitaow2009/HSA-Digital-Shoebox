import csv

def add_expense():
    print("\n--- Add New HSA EOB ---")
    date = input("Service Date (YYYY-MM-DD): ")
    provider = input("Healthcare Provider: ")
    amount = input("Member Responsibility (Amount Paid): ")
    
    # Logic to save to your Digital Shoe-box
    with open('hsa_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, provider, amount, "Unreimbursed"])
    print("Expense logged successfully!")

if __name__ == "__main__":
    add_expense()