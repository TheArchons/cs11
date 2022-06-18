import random

vehicles = ["cybertruck", "beat-up toyota camry", "sailboat", "motorhome"]
places = ["Ohio", "Revelstoke", "the moon", "Wendy's"]

#generate a number between 0 and 3 (to pick a vehicle)
vehicleIndex = random.randint(0,3)

#generate another number between 0 and 3 (to pick a place)
placeIndex = random.randint(0,3)

#print out a song title using the vehicle and place
print("We built", places[placeIndex], "(" + vehicles[vehicleIndex], "Edition)") # We built this city (vehicle Edition)