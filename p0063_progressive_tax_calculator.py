# Question: Build a progressive tax calculator

# English Video: https://www.youtube.com/watch?v=0HeyS1Z2OZY
# Tamil Video: https://www.youtube.com/watch?v=nFEnGwp-wkY

def Grow_With_Data(income, bracket):
    total_tax = 0
    for bracket in brackets:
        bracket_income, rate = bracket
        if bracket_income is None:
            taxable_income = income
        else:
            taxable_income = min(income, bracket_income)

        total_tax = total_tax + taxable_income * rate
        income = income - taxable_income

        if income <= 0:
            break
    return total_tax
assert Grow_With_Data(50000, [(10000, 0.1),(20000, 0.2),(10000, 0.3),(None, 0.4)]) == 12000
assert Grow_With_Data(15000, [(10000, 0.1),(20000, 0.2),(10000, 0.3),(None, 0.4)]) == 2000
print('Passed!')
