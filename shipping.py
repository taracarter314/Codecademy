import random
weight = 41.5
#^Change this to see the price for both ground and premium.
#random.randint(1,20) - to be used if we randomize the weight.
ground_flat_charge = 20

price_per_pound = weight * 1.50
price_per_pound_6 = weight * 3.00
price_per_pound_10 = weight * 4.00
price_per_pound_above = weight * 4.75

cost = price_per_pound + ground_flat_charge
cost2 = price_per_pound_6 + ground_flat_charge
cost3 = price_per_pound_10 + ground_flat_charge
cost4 = price_per_pound_above + ground_flat_charge

premium_flat_charge = 125

premium_per_pound = 4.50
premium_per_pound_6 = 9.00
premium_per_pound_10 = 12.00
premium_per_pound_above = 14.25

cost5 = premium_flat_charge + premium_per_pound
cost6 = premium_flat_charge + premium_per_pound_6
cost7 = premium_flat_charge + premium_per_pound_10
cost8 = premium_flat_charge + premium_per_pound_above

#ground shipping
if weight <=2:
  print(price_per_pound, "+", ground_flat_charge, "=", cost)
elif weight >2 and weight <6:
  print(price_per_pound_6, "+", ground_flat_charge, "=", cost2)
elif weight >6 and weight <10:
  print(price_per_pound_10, "+", ground_flat_charge, "=", cost3)
else:
  print(price_per_pound_above, "+", ground_flat_charge, "=", cost4)

print("We also have Premium Shipping available.")
  
#Drone Shipping
if weight <=2:
  print(premium_per_pound, "+", premium_flat_charge, "=", cost5)
elif weight >2 and weight <6:
  print(premium_per_pound_6, "+", premium_flat_charge, "=", cost6)
elif weight >6 and weight <10:
  print(premium_per_pound_10, "+", premium_flat_charge, "=", cost7)
else:
  print(premium_per_pound_above, "+", premium_flat_charge, "=", cost8)
  
