available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
#deleting keys from dictionary and replacing health with value with 0. This also updates the health points.
health_points += available_items.pop('stamina grains', 0)
health_points += available_items.pop ('power stew', 0)
health_points += available_items.pop('mystic bread', 0)

print(available_items)
print("health points = ", health_points)
# output
# {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25} 
# health_points = 65
