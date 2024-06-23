import os

# The commented out variable is how I would probably set it up but since I don't know the system
# that this will be running on I can't really specify a path... So the way I coded it will show the
# current running directory...

# Path = input("Enter the directory path you want to print the contents of: ")

def list_directory_contents():
    print(os.listdir())

try:
    list_directory_contents()
except NotADirectoryError as err:
    print("Directory does not exist")
