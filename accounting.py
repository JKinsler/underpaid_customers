"""Parses customer data. Compares customer's
amount paid with amount owed."""

# Read through accounting.py and understand what it’s doing.
# Create a function that takes in a text file of customer orders and parses it to produce similar output.
# Add comments explaining what your code is doing.

    
def collect_order(each_line):
  """strips the line and splits it into components.
  Each line should correspond to an order. 
  This is preliminary preparation for order analysis."""
    
  #strips white space off the right side of the line
  each_line = each_line.rstrip()

  #split the line string into multiple elements, store them in a list
  order_info = each_line.split("|") #split the lines
  #print(type(split_order))
  return order_info


def analyze_order(clean_list):
  """Gives the names of customers that did not pay the proper amount owed.
  Takes in a list of information about the customer order.
  Uses the list to compare whether amount paid and amount owed are equivalent."""

  #order_number = clean_line[0]
  customer_name = clean_list[1] 
  customer_paid = float(clean_list[2])
  customer_owed = float(clean_list[3])
  #difference = customer_owed - customer_paid
    
  if customer_paid != customer_owed:
    print(f"{customer_name} owed {customer_owed}, but paid {customer_paid}.")

  return None
    
#get order history from a text file
order_log = open("customer-orders.txt")

for line in order_log: #read each line in the order_log 
  parsed_order = collect_order(line)
  with_balance = analyze_order(parsed_order)


#identify_underpaid_orders(order_dictionary)
# customer_order = parse_customer_orders(order_log)
# print(customer_order)

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
