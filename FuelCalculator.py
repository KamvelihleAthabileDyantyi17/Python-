kilometers = float(input("Enter kilometers: "   ))
PetrolPrice = float(input("Enter petrol price: "))

# 3. Assume their car uses exactly 1 liter for every 10 kilometers.
# Just use the formula they gave you (no input needed!)
liters_needed = kilometers / 10

# 4. Calculate the total cost.
total_cost = liters_needed * PetrolPrice

# 5. Format the final cost to 2 decimal places using round() and print it.
final_cost = round(total_cost, 2)
print(f"The total cost of your trip will be R{final_cost}")