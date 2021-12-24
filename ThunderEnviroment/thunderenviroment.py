import json
json.dump

def str2bool(text: str):
    match text:
        case "true":
            return True
        case "false":
            return False
        case _:
            return False

def bool2str(state: bool):
    match state:
        case True: return "true"
        case False: return "false"
        case _: return None

class Enviroment:
    def __init__(self, file_name: str):
        self.file = open(file_name, 'r+', encoding='utf-8')
        self.file_name = file_name

        self.data = {}
        for line in self.file.readlines():
            try:
                left = line.split(" ", maxsplit=2)[0]
                operator = line.split(" ", maxsplit=2)[1]
                right = line.split(" ", maxsplit=2)[2]
            except: raise Exception("Enviroment Reading Error: Line is invalid!")
            
            match operator:
                case "i->":
                    try:
                        self.data[left] = float(right)
                    except: raise Exception("Enviroment Reading Error: Value of %s can't be converted to float!" % left)
                case "s->":
                    try:
                        self.data[left] = str(right).replace("\\n", "\n")
                    except: raise Exception("Enviroment Reading Error: Value of %s can't be converted to string!" % left)
                case "b->":
                    try:
                        self.data[left] = str2bool(right)
                    except: raise Exception("Enviroment Reading Error: Value of %s can't be converted to boolean!" % left)
                case _:
                    raise Exception("Enviroment Reading Error: Unknown Operator!")
    
    def save(self):
        vars = []
        for variable in self.data.items():
            if type(variable[1]) == int or type(variable[1]) == float:
                vars.append("%s %s %s" % (variable[0], "i->", variable[1]))
            if type(variable[1]) == str:
                vars.append("%s %s %s" % (variable[0], "s->", str(variable[1]).replace("\n", "\\n")))
            if type(variable[1]) == bool:
                vars.append("%s %s %s" % (variable[0], "b->", bool2str(variable[1])))
        
        self.file = open(self.file_name, 'w', encoding='utf-8')
        self.file.write("\n".join(vars))
        self.file = open(self.file_name, 'r+', encoding="utf-8")