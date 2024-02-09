#SYED ABRAR Q2
import math
# for  calculating the  Euclidean distance between two vectors to use in knn...
def calculate_euclidean_distance(vector1, vector2):
    #  dimensions of both vectors matching or not checking
    if len(vector1) != len(vector2):
        raise ValueError("Vector dimensions must match")
    distance = 0
    
    # Calculating the squaring the differences and adding them
    for i in range(len(vector1)):
        distance += (vector1[i] - vector2[i])**2
    return math.sqrt(distance)

# Function to classify the k-nearest neighbors(knn)
def classify_k_nearest_neighbors(training_data, test_instance, k):
    # distances between the test instance and all training instances
    distances = []
    for train_instance, label in training_data:
        distance = calculate_euclidean_distance(train_instance, test_instance)
        distances.append((distance, label))

    # sorting the distances in acsending order
    distances.sort(key=lambda x: x[0])

    # Selecting  the k-nearest neighbors from the order
    neighbors = distances[:k]

    # Counting the votes for each class among the neighbors
    class_votes = {}
    for _, label in neighbors:
        class_votes[label] = class_votes.get(label, 0) + 1
    return max(class_votes, key=class_votes.get)

# Main function to run the code
if __name__ == "__main__":
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    print("Euclidean distance:", calculate_euclidean_distance(vector1, vector2))
    dataset = [([1, 2], 'A'), ([2, 3], 'B'), ([3, 4], 'A')]

    test_instance = [1.5, 2.5]
    k_value = 2
#printing th epredicted labels
    print("Predicted Label : ", classify_k_nearest_neighbors(dataset, test_instance, k_value))
