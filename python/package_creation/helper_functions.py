def do_somthing_random(name):
    print(f"Hello sir{name}",end="\n")
    print(f'we welcome you at cyberz for signing up as {name}')


def make_a_choice(*args):
    """Provide this function a list so that you can get a random choice every time"""
    import random
    choice=random.choice(args)
    return choice


# Standard libraries 
import os
os.getcwd()


import random

listt=["head","tail"]

random.choice(listt)

import shutil
# Copyning a file 
shutil.copyfile('..\example.txt','destination.txt')