import os

def print_directory_contents(path):
    # function will takes a directory path as an argument and prints its contents. 
    print(f"Contents of directory: {path}")

    # List all files and subdirectories in the given directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item) # joins the specified path and item to create the full path to the file or subdirectory.

        # Check if the item is a file or a subdirectory
        if os.path.isfile(item_path):  # check if the given path points to a file or a directory, respectively.
            print(f"File: {item_path}")  
        elif os.path.isdir(item_path):    #Sama as up
            print(f"Directory: {item_path}")
            # Recursively print the contents of subdirectories
            print_directory_contents(item_path)

# Replace 'your_directory_path' with the path of the directory you want to inspect
directory_path = 'your_directory_path'
print_directory_contents(directory_path)
