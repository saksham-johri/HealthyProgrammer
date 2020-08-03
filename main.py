"""
!HealthyProgrammer
*Reminds the Pogrammer to Drink Water, Do Eyes Exercise, and to Do Physical Exercise at certain Time Interwals
"""

from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stop):
    """To Play Music/ Alarm/ Sound

    Args:
        file (mp3): File(mp3) to play
        stop (stopper): Keyword to stop music/ alarm/ sound
    """
    try:
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()

        while True:
            a = input()
            if a == stop:
                mixer.music.stop()
                break

    except Exception as e:
        print(e)

def log(msg):
    """To Maintain The Logs Of HealthyProgrammer In A File With TimeStamp

    Args:
        msg (String): Message to stope in file in form of test/ log
    """
    with open('my_logs.txt', 'a') as f:
        f.write(f"{msg} [ {datetime.now()} ]\n")

if __name__ == "__main__":
    
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    water = 5        #! Gap to Drink Water (in seconds)
    eyes = 10        #! Gap to Do Eyes Extercise (in seconds)
    exercise = 20    #! Gap to Do Physical Exercise (in seconds)

    while True:

        if time() - init_water > water:
            print("\n********  Drink Water!!  ********\n")
            print("Enter 'water' to stop the alarm")
            musicloop('water.mp3', 'water')     #! water.mp3
            log("Drank Water At:")
            init_water = time()
        
        if time() - init_eyes > eyes:
            print("\n********  Do Eyes Exercise!!  ********\n")
            print("Enter 'eyes' to stop the alarm")
            musicloop('eyes.mp3', 'eyes')       #! eyes.mp3
            log("Eyes Exercise Done At:")
            init_eyes = time()

        if time() - init_exercise > exercise:
            print("\n********  Do Physical Exercise!!  ********\n")
            print("Enter 'phy' to stop the alarm")
            musicloop('phy.mp3', 'phy')         #! phy.mp3
            log("Physical Exercise Done At:")
            init_exercise = time()