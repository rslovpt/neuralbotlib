from scripts.json import json_ex
from scripts.memory_access import memory_access
from difflib import SequenceMatcher
import os, importlib
class network:
    def __init__(self):
        self.attitude = []

        self.character_avoidance = ['.', '/', '[', ']', '"', "'", '!', '?', ','],
        self.time_take = 0

    def network_addition(self, word, context):
        return

    def generate_response(self, words_list):
        json_mem = json_ex('mem\set\mem.json').load_file()
        response = None
        top_dif = 1
        for v in json_mem["SENTENCES"]:
            k_words = []
            k_word = ""
            for i in v:
                if i != " ":
                    if v.index(i) == len(v)-1 or v[v.index(i)+1] in self.character_avoidance:
                        k_word += i

                        k_words.append(k_word)
                        k_word = ""
                    else:
                        k_word += i 
                else:
                    k_words.append(k_word.lower())
                    k_word = ""

            if k_word != "":
                k_words.append(k_word)
                k_word = ""
            
            difference = 1

            for i in words_list:
                for z in k_words:
                    if i.lower() == z.lower():
                        difference -= 0.1
                    else:
                        if difference+0.05 >= 1:
                            difference = 1
                        else:
                            difference += 0.05

            if difference < top_dif: 
                top_dif = difference
                rstring = ""
                for i in words_list:
                    if words_list.index(i) == len(words_list):
                        rstring += i
                    else:
                        rstring += i+" "
                response=rstring
            
        return response


    def attain_dict_list(self, list_name):
        json_dict = json_ex('mem\set\dict.json').load_file()
        loaded_item = None
        for name,v in json_dict.items():
            if name.lower() == list_name.lower():
                loaded_item = v[0]
        return loaded_item

    def attain_analyze_files(self):
        files = {}
        for path_distribute in os.listdir(os.path.join("scripts","network_analyze")):
            for c_file in os.listdir(os.path.join("scripts","network_analyze", path_distribute)):
                if c_file[c_file.find('.'):] == ".py":
                    module = importlib.import_module('scripts.network_analyze.'+str(path_distribute)+'.'+str(c_file[:c_file.find('.')]), package=None)
                    files[path_distribute] = module.NET
                else:
                    pass
        return files

    def analyze(self, k_words):
        anlz_files = self.attain_analyze_files()
        response = []

        anlz_config = {
            'InitWords': False
        }

        for i in k_words:
            if k_words.index(i)+1 != len(k_words):
                context = i[1]
                if 'STARTUP' in context:
                    if 'GREETING' in context:
                        if not anlz_config["InitWords"]:
                            response.append(anlz_files['STARTUP']().r(None, self.attain_dict_list(list_name="GREETING")))
                            anlz_config["InitWords"]=True
                    elif 'FAREWELL' in context:
                        if not anlz_config["InitWords"]:
                            response.append(anlz_files['ENDUP']().r(None, self.attain_dict_list(list_name="FAREWELL")))
                            anlz_config["InitWords"]=True
                elif 'ENDUP' in context:
                    if 'FAREWELL' in context:
                        if not anlz_config["InitWords"]:
                            response.append(anlz_files['ENDUP']().r(None, self.attain_dict_list(list_name="FAREWELL")))
                            anlz_config["InitWords"]=True                        
        return response

    def format_language(self, k_words):
        returned_list = []
        cancelled_list = []
        json_dict = json_ex('mem\set\dict.json').load_file()

        for y in k_words:
            for _,v in json_dict.items():
                for i in v:
                    if v.index(i) == 0:
                        for z in i:
                            similarity_ratio = SequenceMatcher(None, y.lower(), z.lower()).ratio()
                            if similarity_ratio > 0.8:
                                data_list = [z.lower(), v[1]]
                                returned_list.append(data_list)
                            else:
                                if y.lower() not in cancelled_list:
                                    cancelled_list.append(y.lower())
        returned_list.append(cancelled_list)
        return returned_list

    def input_recieved(self, text):
        k_words = []
        current_k_word = ""

        for i in text:
            if i != " ":
                if i in self.character_avoidance:
                    pass
                else:
                    if text.index(i) == len(text)-1 or text[text.index(i)+1] in self.character_avoidance:
                        current_k_word += i

                        k_words.append(current_k_word)
                        current_k_word = ""
                    else:
                        current_k_word += i
            else:
                k_words.append(current_k_word)
                current_k_word = ""

        if current_k_word != "":
            k_words.append(current_k_word)
            current_k_word = ""

        established_words = self.format_language(k_words)
        generated_response = self.generate_response(self.analyze(established_words))
        try:
            memory_access(True).memory_addition('mem.json', {
                'user_response': text.strip(),
                'generated_response': generated_response.strip(),
                'process_time': self.time_take
            })
        except AttributeError:
            pass # ERROR LOG GOES HERE

        return generated_response
