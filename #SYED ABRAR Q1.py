#SYED ABRAR Q1
import math

def calculate_euclidean_distance(x, y):
    # For Calculating the  Euclidean distance between two points.
    distance = 0
    for i in range(len(x)):
       distance += (x[i] - y[i]) ** 2
    return math.sqrt(distance)

def calculate_manhattan_distance(x, y):
    # to calculate the  Manhattan distance between two points
    distance = 0
    for i in range(len(x)):
        distance += abs(x[i] - y[i])
    return distance

x_coords = [1, 2, 3, 4]
y_coords = [1, 2, 3, 4]

# finction call to ccalculate the Euclidean distance
euclidean_result = calculate_euclidean_distance(x_coords, y_coords)
print("Euclidean distance:", euclidean_result)

# function call to calculate the  Manhattan distance
manhattan_result = calculate_manhattan_distance(x_coords, y_coords)
print("Manhattan distance:", manhattan_result)
