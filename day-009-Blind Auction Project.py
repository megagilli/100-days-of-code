# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)

# or
# import art
# print(art.logo)

continue_bidding=True

#compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder

    print(f"The winner is {winner} with a highest bid of {highest_bid}")

bid={}
while continue_bidding :
    print("Welcome to the blind Auction!")
    name = input("Whats your name? ")
    price = int(input("whats your bidding amount? $"))
    bid[name]=price
    should_continue=input("Are there any  more bidders left, Type 'yes' or 'no'\n").lower()


    if should_continue=="no":
        continue_bidding=False
        find_highest_bidder(bid)

    elif should_continue=="yes":
        print("\n" * 20)





