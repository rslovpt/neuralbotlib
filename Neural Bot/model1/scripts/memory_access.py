from scripts.json import json_ex
class memory_access:
    def __init__(self, timed_use=False):
        self.tu = timed_use
        self.file = open('history', 'a+')

    def memory_addition(self, dirName, value):
        current_memory = json_ex(f'mem\set\{dirName}').load_file()
        current_memory["MEMORY"].append(value)
        json_ex(f'mem\set\{dirName}').jsonfile_replacement(current_memory)
        
        if self.file.readlines() == []:
            info = f'<user: {value["user_response"]} / bot: {value["generated_response"]}> (process time: {value["process_time"]})' + "\n"
            self.file.write(info)
        else:
            info = f'<user: {value["user_response"]} / bot: {value["generated_response"]}> (process time: {value["process_time"]})' + "\n"
            self.file.writelines(self.file.readlines().append(info))

    def memory_direct_access(self, dirName, value):
        return