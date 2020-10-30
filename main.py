from my_modules.file_manipulator import FileManipulator

file = FileManipulator('letter.txt', 'r')

print(file.read_file())
