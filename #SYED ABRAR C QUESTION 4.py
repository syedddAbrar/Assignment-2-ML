def display_table(header, data):
    # Function to print the header data in a tabular format....
    print(','.join(header))
    for row in data:
        print(','.join(row))

def one_hot_encode_categorical(column):
    # Function for to performing the one-hot encoding on to the  categorical column
    unique_values = list(set(column))
    encoding_dict = {value: i for i, value in enumerate(unique_values)}
    
    encoded_data = []
    
    for value in column:
        encoding = [0] * len(unique_values)
        encoding[encoding_dict[value]] = 1
        encoded_data.append(encoding)
    
    return encoded_data


def load_csv(file_path):
    # Function for to load the CSV file and to extract the header and data.
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
    return header, data


#for Including the file path...
file_path = 'C:\\Users\\SACHIN.R\\Downloads\\archive\\cars_ds_final_2021.csv'
header, data = load_csv(file_path)

# categorical column for the one-hot encoding...
categorical_column_name = 'Drivetrain'
column_index = header.index(categorical_column_name)
categorical_column = [row[column_index] for row in data]

# Applying one-hot encoding on  categorical column
encoded_data = one_hot_encode_categorical(categorical_column)

# Adding one-hot encoded columns on to data....
for i, unique_value in enumerate(set(categorical_column)):
    new_column_name = f"{categorical_column_name}_{i}"
    header.append(new_column_name)
    new_column = [row[i] for row in encoded_data]
    for j in range(len(data)):
        data[j].append(str(new_column[j]))

# for printing the updated dataset
display_table(header, data)
