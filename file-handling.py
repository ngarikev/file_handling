def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.readlines()
        
        # Modify content (e.g., converting to uppercase)
        modified_content = [line.upper() for line in content]
        
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)
        
        print(f"Modified content written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read the file.")

# Run the function
read_and_modify_file()
