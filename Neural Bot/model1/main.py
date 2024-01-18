from scripts.main_network import network
from scripts.json import json_ex as js
from scripts.speech_rec import speech_rec as sr
from scripts.tts import text_to_speech as tts
from scripts.interface import interface as ui

system_booted = False

modules = {}

settings = {
    'speaking_enabled':False,
    'speech_rec_enabled':False,

    'interface_enabled': True,
}

class Boot:
    
    def __init__(self):
        modules['network'] = network()
        if settings['speaking_enabled']:
            modules['tts'] = tts(js("VOICE").load_var())
            modules['tts'].load_module()
        if settings['speech_rec_enabled']:
            modules['sr'] = sr()
            modules['sr'].load_module()
        if settings['interface_enabled']:
            modules['ui'] = ui(size=(1280, 720))
            modules['ui'].load_module()

        global system_booted
        system_booted = True
        print("Modules Loaded: " + str(len(modules)))

        return

Boot()

while (1):
    if system_booted:
        inputed = None
        response = None

        interface_inputed = None

        if not settings['interface_enabled']:
            if settings['speech_rec_enabled']:
                pass
            else:
                inputed = input("Talk >> ")
        else:
            returned_ = modules['ui'].await_input()
            if returned_ != None:
                interface_inputed = returned_[1]
            else:
                interface_inputed = None
        
        if settings['interface_enabled'] and interface_inputed != None:
            response = modules['network'].input_recieved(inputed)
        elif not settings['interface_enabled']:
            response = modules['network'].input_recieved(inputed)

        if settings['interface_enabled']:
            if interface_inputed:
                if settings['speaking_enabled']:
                    pass
                modules['ui'].return_output(response)
            modules['ui'].display()
        else:
            if settings['speaking_enabled']:
                pass
            else:
                print(response)