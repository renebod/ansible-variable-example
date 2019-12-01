#!/usr/bin/env python
import os
import random

def welkom():
    return "Welkom " + os.environ.get('USER', 'unknown')

def get_number():
    return random.randint(77,591)

def get_other():
    return random.choice(["35", "12", "41", "30"])
