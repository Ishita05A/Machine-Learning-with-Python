high_income = True
good_income = True
if high_income and good_income:
    print("Eligible")
else:
    print("Not Eligible")

high_income = False
good_income = True
if high_income or good_income:
    print("Eligible")
else:
    print("Not Eligible")

high_income = False
good_income = True
if not good_income:
    print("Eligible")
else:
    print("Not Eligible")
