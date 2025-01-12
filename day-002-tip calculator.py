print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What percent tip would you like to give? 10 12 15"))
people=int(input("How many peole toi split the bill?"))
bill_with_tip=tip/100*bill+bill
split_bill = (bill_with_tip/people)
final_amount=(round(split_bill,2))
print(f"Each person should pay: ${final_amount}")