# Speed data (km/h)
speed = [0, 35, 43, 33, 29, 25, 35, 33, 21, 16, 12, 44, 47, 4, 47, 37, 13, 32, 21, 0]

# Distance covered each minute (km)
distance_each_min = []

for s in speed:
    distance_each_min.append(s * (1/60))

# Total calculated distance
calculated_distance = sum(distance_each_min)

# Actual distance from Google Maps (ENTER VALUE HERE)
actual_distance = 10.0   # km (change if different)

# Percentage error
percentage_error = abs(actual_distance - calculated_distance) / actual_distance * 100

print("Calculated distance (km):", round(calculated_distance, 2))
print("Actual distance (km):", actual_distance)
print("Percentage error (%):", round(percentage_error, 2))
