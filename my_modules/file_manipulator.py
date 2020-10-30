
class FileManipulator:
    """ Class to Handle Manipulation of Files """

    # Class Constructor
    def __init__(self, file_name, open_mode):
        # File Attributes
        self.__file_name = file_name
        self.__open_mode = open_mode
        self.__pointer = self.open_file()

    # Method to Open File
    def open_file(self):
        try:
            # Open File
            # with open(self.__file_name, self.open_mode) as f:
            pointer = open(self.__file_name, self.__open_mode)
            return pointer
        except Exception as e:
            return e

    # Read Content From File
    def read_file(self):
        try:
            pointer = self.__pointer
            counter = 1
            for line in pointer:
                print(f'{counter}. {line}')
                counter += 1
            pointer.close()
        except Exception as e:
            print(e)
        # readd = self.__pointer.readline()
        # return readd
