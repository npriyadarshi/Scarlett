from datetime import datetime

from GreyMatter.SenseCells.tts import tts

def what_is_time():
    tts("The time at your current place is"+datetime.strftime(datetime.now(),'%H:%M:%S'))
