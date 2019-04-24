# coding: utf-8

class ReadFile:
    def __init__(self, file_path, file_name):
        try:
            file = open(file_path + file_name)
            self.__code = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
    def get_code(self):
        return self.__code

