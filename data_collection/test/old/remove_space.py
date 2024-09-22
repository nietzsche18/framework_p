# open the file for reading
with open(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv', 'r') as file:
    file_contents = file.read()

# replace all occurrences of ", " with ","
modified_contents = file_contents.replace(', ', ',')

# open the file for writing and save the modified contents
with open(r'C:\Users\33670\Desktop\framework\data_collection\historical_data\full.csv', 'w') as file:
    file.write(modified_contents)
