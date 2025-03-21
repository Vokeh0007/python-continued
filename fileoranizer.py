import os
import shutil

# Define the directory to organize
source_directory = input("Enter the directory path to organize: ")

# Define the categories for different types of files
file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents": ['.pdf', '.txt', '.docx', '.doc', '.xls', '.ppt', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac'],
    "Videos": ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    "Archives": ['.zip', '.tar', '.gz', '.rar', '.7z'],
    "Code": ['.py', '.js', '.html', '.css', '.java', '.cpp'],
    #
    "Others": []  # This will catch anything that doesn't match the above types
}

def organize_files(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Loop through the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find the category for the file
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions or (not extensions and file_extension not in file_types):
                category_folder = os.path.join(directory, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                new_file_path = os.path.join(category_folder, filename)

                # Move the file to the new category folder
                shutil.move(file_path, new_file_path)
                print(f"Moved {filename} to {category_folder}")
                moved = True
                break
        
        # If file type does not match any category, move it to 'Others'
        if not moved:
            others_folder = os.path.join(directory, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            new_file_path = os.path.join(others_folder, filename)
            shutil.move(file_path, new_file_path)
            print(f"Moved {filename} to {others_folder}")

# Run the organizer
organize_files(source_directory)
