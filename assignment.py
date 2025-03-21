def modify_content(text):

    #convert to uppercase
    return text[::-1].upper()

try:
    filename = input("Enter the name of the file to read: ")
    
    with open(filename, "r") as file:
        content = file.read()
        
    modified_content = modify_content(content)
    
    new_filename = 'modified_' + filename
    with open(new_filename, "w") as file:
        file.write(modified_content)
        
        
    print(f"Mofified content written to {new_filename}")
    
    
except FileNotFoundError:
    print("Error: The file {filename} was not found.")
except PermissionError:
    print("Error: Permission denied to read the file {filename}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
