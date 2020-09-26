# User input for proceeds and costs of the company
proceeds = int(input("Hello, enter proceeds of company: "))
costs = int(input("Enter costs of company : "))

# Find out profit or lesion; profit = proceeds - costs

if proceeds > costs:
    profit = proceeds - costs
    print(f"Your company profit equivalent to {profit}")
    employees = int(input("How many employees you have? "))
    profit_per_employee = profit / employees
    print(f"Company profit per employee will be: {profit_per_employee}")
else:
    print("Company operates at a loss for itself. Costs are more than proceeds.")
