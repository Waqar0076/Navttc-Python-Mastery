# print("Hello World!")

## Working with modules

# module for checking directory
import os
print(os.listdir())

# module for printing calender
import calendar
year = 2025
month = 3
print(calendar.month(year, month))

## External Modules 

# module for playing Sound
from playsound import playsound # type: ignore
playsound('music.mp3')

# another module for playing Sound
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("music.mp3")
play_obj = wave_obj.play()
play_obj.wait_done()













