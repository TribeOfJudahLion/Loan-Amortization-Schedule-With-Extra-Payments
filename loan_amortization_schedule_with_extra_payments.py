import pandas as pd


def calculate_amortization_schedule(loan_amount, annual_interest_rate, years, extra_payments):
    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100

    # Total number of payments
    total_payments = years * 12

    # Monthly payment calculation
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / (
                (1 + monthly_interest_rate) ** total_payments - 1)

    # Initialize amortization schedule
    schedule = []
    remaining_balance = loan_amount

    for month in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        extra_payment = extra_payments.get(month, 0)
        total_payment = monthly_payment + extra_payment

        # Apply extra payment
        principal_payment += extra_payment
        if principal_payment > remaining_balance:
            principal_payment = remaining_balance
            total_payment = interest_payment + principal_payment

        # Update remaining balance
        remaining_balance -= principal_payment

        # Add to schedule
        schedule.append([month, monthly_payment, extra_payment, total_payment, principal_payment, interest_payment,
                         remaining_balance])

        if remaining_balance <= 0:
            break

    # Convert to DataFrame for better visualization
    schedule_df = pd.DataFrame(schedule,
                               columns=["Payment Number", "Scheduled Payment", "Extra Payment", "Total Payment",
                                        "Principal Paid", "Interest Paid", "Remaining Balance"])

    # Summary
    total_interest = schedule_df["Interest Paid"].sum()
    total_principal = schedule_df["Principal Paid"].sum()
    time_saved = years * 12 - len(schedule_df)

    summary = {
        "Total Principal Paid": total_principal,
        "Total Interest Paid": total_interest,
        "Time Saved (months)": time_saved
    }

    return schedule_df, summary


# Example usage:
loan_amount = 200000  # $200,000 loan
annual_interest_rate = 4.5  # 4.5% annual interest
years = 30  # 30 year mortgage
extra_payments = {12: 1000, 24: 1000, 36: 1000}  # Extra payments of $1000 at the end of year 1, 2, and 3

schedule, summary = calculate_amortization_schedule(loan_amount, annual_interest_rate, years, extra_payments)

# Displaying first few rows of the schedule and the summary
print(schedule.head())
print("\nSummary:\n", summary)
