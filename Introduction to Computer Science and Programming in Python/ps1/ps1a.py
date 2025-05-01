portion_down_payment = 0.25 
annual_return = 0.04  # Assumed annual investment return rate

# User inputs
total_cost = float(input("Total cost of the house: "))
annual_salary = float(input("Annual salary: "))
portion_saved = float(input("Portion of salary to be saved (e.g., 0.1 for 10%): "))
semi_annual_raise = float(input("Semi-annual raise (e.g., 0.07 for 7%): "))

# Calculated values
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
current_savings = 0.0
months = 0

# Loop until we reach the down payment
while current_savings < down_payment:
    # Add monthly savings
    current_savings += current_savings * (annual_return / 12)  # investment return
    current_savings += portion_saved * monthly_salary          # salary savings
    
    months += 1

    # Apply semi-annual raise every 6 months
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

# Final result
print("Number of months to save for down payment:", months)
