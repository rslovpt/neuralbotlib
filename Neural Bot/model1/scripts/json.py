from decouple import config
import json

class json_ex:
    def __init__(self, var):
        self.var = var
        
    def load_var(self):
        return json.load(config(self.var))

    def load_file(self):
        f = open(self.var)
        data = json.load(f)
        f.close()
        return data

    def dump_var(self):
        return json.dumps(self.var)

    def jsonfile_replacement(self, new_value):
        open(self.var,'r+').close()
        json.dump(new_value, open(self.var, 'w+'))