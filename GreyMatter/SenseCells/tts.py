import os
def tts(message):
    return os.system('espeak '+'"'+message+'"')
