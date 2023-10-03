# Define input and output file paths
input_file_path = 'para.txt'
output_file_path = 'output.txt'

# Open input file and create output file, appending ',,,,,,' to each line
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Read each line from the input file, append ',,,,,,' and write to the output file
    for line in input_file:
        modified_line = line.strip() + ',,,,,,\n'  # Add ',,,,,,' and newline character
        output_file.write(modified_line)

print("File modified and saved successfully.")
