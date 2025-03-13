def calculate_cash_flow(rental_income, mortgage, property_tax, insurance, maintenance, utilities, property_management, other_expenses):
    """
    Calculate the monthly cash flow of a rental property.
    """
    total_expenses = (mortgage + property_tax + insurance + maintenance + utilities + property_management + other_expenses)
    cash_flow = rental_income - total_expenses
    
    return cash_flow

# Get user inputs
rental_income = float(input("Enter your monthly rental income: "))
mortgage = float(input("Enter your monthly mortgage payment: "))
property_tax = float(input("Enter your monthly property tax: "))
insurance = float(input("Enter your monthly insurance cost: "))
maintenance = float(input("Enter your estimated monthly maintenance cost: "))
utilities = float(input("Enter your monthly utility expenses (if paid by you): "))
property_management = float(input("Enter your monthly property management fee (if any): "))
other_expenses = float(input("Enter any other monthly expenses: "))

# Calculate cash flow
cash_flow = calculate_cash_flow(rental_income, mortgage, property_tax, insurance, maintenance, utilities, property_management, other_expenses)

# Output the result
if cash_flow > 0:
    print(f"You have a positive cash flow of ${cash_flow:.2f} per month.")
elif cash_flow < 0:
    print(f"You have a negative cash flow of ${cash_flow:.2f} per month.")
else:
    print("You are breaking even with zero cash flow.")