# coding: utf-8

class WriteFile:
    def __init__(self, file_name, code: str, operation: str):
        # 読込むファイルのパスを宣言する
        self.__file_path = "./run_space/"
        if operation == 'w' or operation == 'a':
            try:
                file = open(self.__file_path + file_name, operation)
                file.write(code)
            except Exception as e:
                print(e)
            finally:
                file.close()
        else:
            print("argument 'operation' must be 'w' or 'a' but " + str(operation) )
