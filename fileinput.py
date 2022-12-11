# class FileInput to read a .txt file
class FileInput:
    def __init__(self, filename):
        self.filename = filename

    def __open_file(self):
        try:
            return open(self.filename, 'r')
        except FileNotFoundError:
            print('Error: File not found')
            return None

    def get_content(self):
        file = self.__open_file()
        if file is not None:
            content = file.read()
            file.close()

            if content == '':
                print('Error: File is empty')
                return None
            else:
                return content
        return None
