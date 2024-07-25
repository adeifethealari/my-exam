# This code is incomplete. Fill in the missing parts to calculate the monthly payment.

def calculate_monthly_payment(interest_rate, amount_borrowed, loan_term_years):
     interest_rate = 0.05  # 5% annual interest

     amount_borrowed = 10000

     loan_term_years = 2

    # Hint: Use the formula for monthly loan payment:

     monthly_payment = (amount_borrowed * interest_rate) / (1 - (1 + interest_rate) ** (loan_term_years * 12))

    # Replace the following line with the actual calculation
calculate_monthly_payment()

print("calculate_monthly_payment")






# Example usage (uncomment and test after completing the function)

#interest_rate = 0.05  # 5% annual interest

#amount_borrowed = 10000

#loan_term_years = 2

#monthly_payment = calculate_monthly_payment(interest_rate, amount_borrowed, loan_term_years)

#print(f"Monthly payment: ${monthly_payment:.2f}")