<br/>
<p align="center">
  <h3 align="center">Maximize Your Loan Strategy: Advanced Amortization Schedule with Extra Payments!</h3>

  <p align="center">
    Empower Your Repayments - See How Extra Payments Can Transform Your Loan Journey!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Statement

**Scenario**: 
A borrower named Alex has taken out a mortgage loan of $200,000 at an annual interest rate of 4.5% with a term of 30 years. Alex is interested in understanding how making extra payments at specific intervals will impact the total interest paid over the life of the loan, the time required to pay off the loan, and the monthly payment structure.

**Challenge**: 
Alex is not sure how to calculate the impact of these extra payments on the loan's amortization schedule. He needs a way to visualize how each payment, both regular and extra, affects the principal and interest over the loan's term. Additionally, he wants to know the total interest paid and the time saved due to these extra payments.

### Solution

**Approach**:
We use the `calculate_amortization_schedule` function to create a detailed amortization schedule for Alex's loan. This function will take into account the loan amount, annual interest rate, loan term, and any extra payments made.

**Parameters Used**:
- `loan_amount`: $200,000 (the initial loan amount).
- `annual_interest_rate`: 4.5% (the annual interest rate of the loan).
- `years`: 30 (the term of the loan in years).
- `extra_payments`: Specified as $1000 at the end of the first, second, and third years (months 12, 24, and 36).

**Function Execution**:
- The function first calculates the monthly interest rate and the total number of payments.
- It then calculates the standard monthly payment without considering extra payments.
- For each month, it calculates the interest and principal parts of the payment, adjusts for any extra payment, and updates the remaining balance of the loan.
- The function stores each month's details in a DataFrame and also calculates a summary of total interest paid and time saved.

**Output**:
1. **Amortization Schedule (DataFrame)**: This table shows details for each monthly payment, including the payment number, scheduled payment amount, extra payment amount, total payment amount, principal paid, interest paid, and the remaining balance on the loan.

2. **Summary (Dictionary)**: This includes the total principal paid over the life of the loan, the total interest paid, and the number of months saved due to the extra payments.

**Benefits for Alex**:
- **Clarity on Payment Structure**: Alex can see how each payment is split between principal and interest.
- **Impact of Extra Payments**: The schedule clearly shows how extra payments reduce the principal faster and decrease the total amount of interest paid over the loan's life.
- **Financial Planning**: The summary provides Alex with the overall financial impact of the loan, helping him in long-term financial planning.

**Conclusion**:
Using this approach, Alex can comprehensively understand the financial implications of his mortgage and the benefits of making extra payments. This information helps him make informed decisions about his loan repayment strategy.

The provided Python function `calculate_amortization_schedule` is designed to compute the amortization schedule for a loan. It takes into account not only regular payments but also allows for extra payments at specified intervals. Here's a breakdown of its logic and functionality:

### Parameters
1. **loan_amount**: The initial amount of the loan.
2. **annual_interest_rate**: The annual interest rate of the loan in percentage.
3. **years**: The term of the loan in years.
4. **extra_payments**: A dictionary where keys are payment numbers (months) and values are the amounts of extra payments.

### Process
1. **Monthly Interest Rate Calculation**: 
   - The annual interest rate is converted into a monthly interest rate by dividing it by 12 and then converting it to a decimal (dividing by 100).

2. **Total Payments Calculation**:
   - The total number of payments over the life of the loan is calculated by multiplying the number of years by 12.

3. **Monthly Payment Calculation**:
   - The standard monthly payment (without considering extra payments) is calculated using the formula for an annuitized payment.

4. **Amortization Schedule Initialization**:
   - A list named `schedule` is initialized to store the details of each payment.
   - The remaining balance of the loan is set to the initial loan amount.

5. **Monthly Calculations**:
   - For each month until the total number of payments:
     - Calculate the interest payment based on the remaining balance.
     - Calculate the principal payment as the difference between the monthly payment and the interest payment.
     - Retrieve the extra payment for the month if any.
     - Update the total payment to include the extra payment.
     - Ensure that the principal payment does not exceed the remaining balance.
     - Reduce the remaining balance by the principal payment.
     - Store all these details in the `schedule` list.
     - End the loop if the remaining balance is paid off.

6. **Conversion to DataFrame**:
   - The schedule list is converted into a pandas DataFrame for better visualization and analysis.

7. **Summary Calculation**:
   - A summary is created that includes the total principal paid, total interest paid, and the time saved in months due to extra payments.

### Output
- The function returns two items:
  1. **schedule_df**: A pandas DataFrame representing the amortization schedule.
  2. **Summary**: A dictionary summarizing the total principal paid, total interest paid, and time saved.

### Example Usage
The example demonstrates the function usage with a $200,000 loan, 4.5% annual interest, over 30 years, with extra payments at the end of years 1, 2, and 3. The first few rows of the schedule and the summary are displayed using `print`.

### Conclusion
This function is a comprehensive tool for calculating the amortization schedule of a loan, taking into account extra payments and their impact on the overall loan term and interest paid. It's beneficial for financial planning and understanding how additional payments can reduce the loan's lifespan and total interest cost.

The output from the `calculate_amortization_schedule` function consists of two parts: the amortization schedule displayed as a pandas DataFrame and a summary dictionary. Let's break down each of these in detail:

### Amortization Schedule DataFrame

1. **Columns**:
   - **Payment Number**: Sequential number of each payment, starting from 1.
   - **Scheduled Payment**: The standard monthly payment amount calculated based on the loan amount, interest rate, and loan term.
   - **Extra Payment**: Any additional payment made in the month over and above the scheduled payment. This is specified by the user.
   - **Total Payment**: The sum of the scheduled and extra payments for the month.
   - **Principal Paid**: The portion of the total payment that goes towards reducing the loan principal.
   - **Interest Paid**: The portion of the total payment that goes towards paying off the interest.
   - **Remaining Balance**: The remaining loan amount after the current month's payment.

2. **Rows**:
   - Each row corresponds to a monthly payment, starting with the first month.
   - The first five rows show the initial stage of the repayment where most of the payment goes towards the interest, and a smaller portion reduces the principal.

3. **Example Data** (First 5 Rows):
   - In the first month, out of the total payment of approximately $1013.37, $750 goes towards interest, and the rest reduces the principal slightly, leaving a remaining balance of about $199,736.63.
   - This trend continues, with each subsequent payment slightly reducing the interest portion and increasing the principal portion, decreasing the remaining balance.

### Summary Dictionary

1. **Total Principal Paid**: 
   - The total amount paid towards the loan principal. In this case, it's approximately $199,999.99, which is essentially the original loan amount.

2. **Total Interest Paid**: 
   - The total amount paid towards interest over the life of the loan. Here, it amounts to approximately $157,436.94.

3. **Time Saved (months)**: 
   - The number of months saved from the original loan term due to making extra payments. In this instance, 10 months are saved, which implies that the loan is paid off earlier than the originally scheduled 30 years.

### Conclusion
This output is valuable for understanding how each payment is allocated between interest and principal, and how extra payments can accelerate the loan payoff and reduce the total interest paid. The summary provides a quick overview of the total costs involved and the benefits of making extra payments.

## Built With

This Amortization Schedule Calculator is developed using a combination of robust programming languages and libraries, ensuring accuracy, efficiency, and ease of use. Below are the key components of our tech stack:

### Python
- **Language**: The core of this project is written in Python, a versatile and widely-used programming language known for its simplicity and readability. Python's extensive library support and community-driven resources make it an ideal choice for financial calculations and data handling.

### Pandas
- **Data Manipulation Library**: We use Pandas, a powerful Python library, for data manipulation and analysis. It is particularly well-suited for dealing with structured data, like our loan amortization schedules. Pandas offer data structures (like DataFrame) and operations for manipulating numerical tables and time series, making it perfect for organizing and presenting the amortization data in a clear and accessible format.

### Financial Calculation
- **Complex Computations**: The script employs standard financial formulas to compute monthly payments, interest, and principal amounts. These calculations are critical in generating accurate amortization schedules and summaries.

### Customizable Payment Schedule
- **Flexibility in Payments**: Our calculator allows for the incorporation of extra payments at specified intervals. This feature provides users with the flexibility to plan their loan repayment more effectively and see the impact of additional payments on their overall loan term and interest.

### User-Friendly Output
- **Clear and Concise Summary**: The output of the script includes a detailed amortization schedule in a DataFrame format and a summary of the total principal and interest paid, along with the time saved by making extra payments. This user-friendly presentation of data helps in better understanding and financial planning.

---

This section should give users and contributors a clear understanding of the technologies and approaches used in your project, emphasizing its functionality and the rationale behind the choice of each component. Remember, a well-documented "Built With" section not only informs but also attracts contributors and users by showcasing the robustness and thoughtfulness of your tech stack.Here are a few examples.

## Getting Started

This section provides a step-by-step guide to help you get started with the Amortization Schedule Calculator. This tool is designed to assist in calculating a detailed amortization schedule for a loan, considering regular and extra payments. It's ideal for personal finance planning, particularly for loans like mortgages.

#### Prerequisites

Before running the calculator, ensure you have the following:

1. **Python**: The script is written in Python, so you need Python installed on your machine. [Download Python](https://www.python.org/downloads/)

2. **Pandas Library**: The script uses Pandas for data manipulation. You can install Pandas via pip:
   ```bash
   pip install pandas
   ```

#### Installation

1. **Clone the Repository**:
   If the script is hosted in a repository, clone it to your local machine:
   ```bash
   git clone [repository-url]
   ```
   Replace `[repository-url]` with the actual URL of the repository.

2. **Navigate to the Script Directory**:
   Change your directory to where the script is located:
   ```bash
   cd path/to/script
   ```
   Replace `path/to/script` with the actual path to the script's directory.

#### Running the Script

1. **Open the Script**:
   Open `loan_amortization_schedule_with_extra_payments.py` in your preferred Python IDE or text editor.

2. **Set Your Loan Parameters**:
   Modify the parameters at the bottom of the script to reflect your specific loan scenario. Here are the parameters you can set:
   - `loan_amount`: The total amount of the loan (e.g., 200000 for $200,000).
   - `annual_interest_rate`: The annual interest rate of the loan in percentage (e.g., 4.5 for 4.5%).
   - `years`: The term of the loan in years (e.g., 30 for a 30-year loan).
   - `extra_payments`: A dictionary where keys are the payment months and values are the extra payment amounts (e.g., `{12: 1000, 24: 1000, 36: 1000}` for extra payments of $1000 at the end of the first, second, and third years).

3. **Run the Script**:
   Execute the script in your Python environment. This can typically be done by navigating to the script directory in your command line and running:
   ```bash
   python loan_amortization_schedule_with_extra_payments.py
   ```
   This will print the first few rows of the amortization schedule and the summary.

#### Interpreting the Output

- The script outputs the amortization schedule as a pandas DataFrame. This schedule includes details like payment number, scheduled payment, extra payment, total payment, principal paid, interest paid, and remaining balance for each month.
- It also provides a summary showing the total principal paid, total interest paid, and time saved due to extra payments.

#### Contributing

- If you're interested in contributing to this project, please read our [Contributing Guidelines](link-to-contributing-guidelines).

---

Remember to replace placeholder links and paths with actual ones. This guide aims to make the process of setting up and using the calculator as seamless as possible for users, regardless of their technical background.

## Roadmap

See the [open issues](https://github.com//Loan-Amortization-Schedule-With-Extra-Payments/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Loan-Amortization-Schedule-With-Extra-Payments/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Loan-Amortization-Schedule-With-Extra-Payments/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Loan-Amortization-Schedule-With-Extra-Payments/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
