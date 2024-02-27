month_expenses = [5200, 6350, 4600, 4130, 3190]
separator = "----------------------"

print(separator)
print(f"January: ₱{month_expenses[0]}")
print(f"February: ₱{month_expenses[1]}")
print(f"March: ₱{month_expenses[2]}")
print(f"April: ₱{month_expenses[3]}")
print(f"May: ₱{month_expenses[4]}")
print(separator)

extra_spending_feb = month_expenses[1] - month_expenses[0]
print("\nIn Feb, how many pesos you spent extra compare to January?")
print("#1 answer:", extra_spending_feb)

first_quarter_expense = sum(month_expenses[:3])
print("\nFind out your total expense in first quarter (first three months) of the year")
print("#2 answer:", first_quarter_expense)

checker_2000 = False
for expense in month_expenses:
    if expense == 2000:
        checker_2000 = True
        break
print("\nDid you spend exactly 2000 pesos in any month?")
print("#3 answer:", checker_2000)

#I didn't used def because it wasn't taught yet
print("\nUpdated expenses after June:")
print("#4 answer:", month_expenses)

month_expenses.append(1980)
print("\n" + separator)
print("Added New Month")
print(f"June: ₱{month_expenses[5]}")
print(separator)

month_expenses[3] -= 200
print("\nExpenses after refund correction in April:")
print("#5 answer:", month_expenses)
