import random
from GreyMatter.SenseCells.tts import tts

def who_are_you():
    messages = ["I am your personal assistant","It's me, Scarlett"]
    tts(random.choice(messages))

def how_am_i():
    replies = ["You rock...my love","Well....I can't get my eyes of you"]
    tts(random.choice(replies))

def undefined():
    tts("I dont konw what that means!")
