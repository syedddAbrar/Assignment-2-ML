#SYED ABRAR C QUESTION 3
import random

def custom_encoeding(input_data):
    # Function is perform custom label encoding on the given input data
    encoding_map = {}
    encoded_values = []

    # we use Seed function for reproducibility
    random.seed(50)

    # For Loop for input data for encoding
    for item in input_data:
        if item not in encoding_map:
            # Maping the random float values to integer for teh encoding
            encoding_map[item] = int(random.random() * 1000)
        encoded_values.append(encoding_map[item])
    
    return encoded_values

def read_dat(file_path):    # Function to read the data from the given file
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Goes through each lines and splits the data
        for line in lines[1:]:
            row = line.strip().split(',')
            data.append(row)
    return data

def main():
    file_path = "D:\SA C\sem 4\MACHINE LEARING\assin 1\DDD.txt"
    dataset = read_dat(file_path)

    target_column = [row[15] for row in dataset]
    encoded_target = custom_encoeding(target_column)

    # Display original and encoded data
    print("target data (original):", target_column)
    print("Target data (Encoded):", encoded_target)

main()
