# Calculate net price with 15% discount and 8% tax

data = input("Enter price :")
price = int(data)    # String to int
discount = price * 15 / 100
discounted_price = price - discount
tax = discounted_price * 8 / 100
net_price = discounted_price + tax

print('Net price = ', net_price)

