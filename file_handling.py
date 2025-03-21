#file handling -- ability to perfom various operations on files like reading and writing
#files are used to store data in a structured way/store data permanently unlike variables
# file handling allows one to read, write, append, delete files
# file handling is done using built-in functions
# open() function is used to open a file
# open(file_name, mode)-- syntax
# file_name -- name of the file to be opened
# mode -- mode in which the file is opened
# modes are:
# 'r' -- read mode -- opens a file for reading
# 'w' -- write mode -- opens a file for writing
# 'a' -- append mode -- opens a file for appending
# 'x' -- exclusive creation -- creates a new file and opens it for writing
# 'b' -- binary mode -- opens a file in binary mode
# reading files -- read() function is used to read a file
# read() -- reads the entire file
# read(n) -- reads n bytes of the file
# readlines() -- reads the entire file and returns a list of lines
# readline() -- reads a single line of the file

#wiriting and appending to files
# write() -- writes a string to a file -- overwrites content
# writelines() -- writes a list of strings to a file
# append() -- appends a string to a file -- adds content to the end of the file without deleting the existing content
# close() -- closes the file


#examples
# The with statement in Python is used for resource management
#wiritng to a file
with open("example.txt", "w") as file:
    file.write("Hello World\n")
    file.write("File handling in python")
    
#reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#reading a file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
#appending to a file
with open("exaple.txt", "a") as file:
    file.write("\n Appending a new line!")

#using tell() and seek() functions
# tell() -- returns the current position of the file pointer
# seek() -- moves the file pointer to a specified position

with open("example.txt", "r") as file:
    print(file.tell())
    file.seek(0)
    print(file.read(10)) # reads the first 10 bytes/characters of the file