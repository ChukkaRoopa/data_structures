expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, how many dollars you spent extra compare to January:", expense[1] - expense[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("Total expense: ", expense[0]+expense[1]+expense[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print("If you spent exactly 2000 in any month: ", 2000 in expense)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print("expense at end of june: " ,expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expense[3] = expense[3] - 200
print(expense)
