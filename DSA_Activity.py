month_expenses = [5200, 6350, 4600, 4130, 3190]

extra_spending_feb = month_expenses[1] - month_expenses[0]
print("In Feb, how many pesos you spent extra compare to January?")
print("#1 answer:", extra_spending_feb)

first_quarter_expense = sum(month_expenses[:3])
print("\nFind out your total expense in first quarter (first three months) of the year")
print("#2 answer:", first_quarter_expense)

spent_2000 = False
for expense in month_expenses:
    if expense == 2000:
        spent_2000 = True
        break
print("\nDid you spend exactly 2000 pesos in any month?")
print("#3 answer:", spent_2000)

month_expenses.append(1980)
print("\nUpdated expenses after June:")
print("#4 answer:", month_expenses)

month_expenses[3] -= 200
print("\nExpenses after refund correction in April:")
print("#5 answer:", month_expenses)
