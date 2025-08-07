from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
bids = {}
bid_active = True
while bid_active:
    name = input("What is your name?: ")
    bid = input("what is your bid?: $")
    # TODO-3: Whether if new bids need to be added
    bids[name] = bid
    user_choice = input("Are there any other bidders? Type 'yes or 'no'.")
    if user_choice.lower() == "yes":
        print("\n" * 20)
    elif user_choice.lower() == "no":
        bid_active = False
# TODO-4: Compare bids in dictionary
winner = ""
max_bid = 0
for bidder in bids:
    current_bid = int(bids[bidder])
    if max_bid <= current_bid:
        max_bid = current_bid
        winner = bidder

print(f"The winner is {winner} with a bid of ${max_bid}")





