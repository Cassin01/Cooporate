from modules import read_file, write_file
import importlib

class RunCode:
    def __init__(self, func_name, file_name):
        header = read_file.ReadFile("./header_footer/", "header.py").get_code()
        code = read_file.ReadFile("./local/local_db/", file_name).get_code()
        footer = read_file.ReadFile("./header_footer/", "footer.py").get_code()

        write_file.WriteFile("runner.py", header + '\n', 'w')
        codef, codeb = self.use_till_find(code, func_name)
        write_file.WriteFile("runner.py", codef, 'a')
        write_file.WriteFile("runner.py", self.gain(file_name, func_name), 'a')
        write_file.WriteFile("runner.py", codeb, 'a')
        write_file.WriteFile("runner.py", footer + '\n', 'a')
    
    def get_val(self):
        m = importlib.import_module('run_space.runner')
        print(m.Runner().get_value())


    def use_till_find(self,lines, module_name):
        codef = ""
        codeb = ""
        f = True
        space4 = '    '
        for line in lines.split("\n"):
            if module_name in line:
                f = False
            if f == True:
                codef += space4 + space4 + line + '\n'
            elif f == False:
                codeb += space4 + space4 + line + '\n'
        return (codef, codeb)

    def gain(self,module_name, func_name):
        indent = '    '
        return indent + indent + "self.__value = " + func_name + '\n'


if __name__ == "__main__":
    r = RunCode("p.get_name()", "tmp.py")
    r.get_val()