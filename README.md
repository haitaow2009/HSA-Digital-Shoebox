# HSA Digital Shoebox

The primary goal is to log medical expenses that you have paid out-of-pocket but have not yet reimbursed from your HSA. Since HSA withdrawals are tax-free at any time in the future if backed by a receipt, this tool acts as a "Digital Shoe-box" for your records.

## Getting Started

For detailed setup instructions, see [SETUP.md](SETUP.md).

## Functional Requirements

The **HSA Digital Shoebox** is designed to perform the following core tasks:

- **Expense Logging:** Capture key details from medical EOBs, including date of service, provider name, and member responsibility (amount paid).
- **Data Persistence:** Automatically save all entries to a local `hsa_data.csv` file for long-term record keeping.
- **Status Tracking:** Categorize each expense as either "Reimbursed" or "Unreimbursed" to track outstanding claims.
- **Financial Summary:** (Coming Soon) Calculate the total balance of all unreimbursed medical expenses.
