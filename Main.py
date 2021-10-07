import os
import sys
import time
import itertools
import threading
from pytube import YouTube
from colorama import Fore as fc
from math import log, floor


# i don't understand this either bro (stack overflow)
def format(number):
    units = ['', 'K', 'M', 'B']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.0f%s' % (number // k**magnitude, units[magnitude])


# for displaying colored output
os.system("")

# taking the url as an input
link = input("Enter the video URL Here \n"+fc.LIGHTCYAN_EX)
print(fc.WHITE)

# Youtube object with the link
try:
    youtube = YouTube(link)
except Exception as e:
    print(fc.LIGHTRED_EX+"Problem Contacting the server,\nPlease Check the URL and try again"+fc.WHITE)
    print("Press Enter To Exit")
    input()
    exit()

print("\nVideo Information:\n\n")

views = str(format(int(youtube.views)))
rating = int((youtube.rating/5)*100)


rating = str(rating)+"%"


# prints the video details
print(fc.LIGHTYELLOW_EX+"Title: "+fc.WHITE+youtube.title)
print(fc.LIGHTYELLOW_EX+"Channel: "+fc.WHITE+youtube.author)
print(fc.LIGHTYELLOW_EX+"Views: "+fc.WHITE+views+" views")
print(f"{fc.LIGHTYELLOW_EX}Rating: {fc.WHITE}{rating}\n")

# gets the desktop path
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

done = False

# animation cycle


def animate():
    for c in itertools.cycle(["Downloading ⢿⡿", "Downloading ⣻⣟", "Downloading ⣽⣯", "Downloading ⣾⣷", "Downloading ⣽⣯", "Downloading ⣻⣟"]):
        if done:
            break
        sys.stdout.write('\r'+fc.LIGHTBLUE_EX+c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()

try:
    video_streams = youtube.streams.get_highest_resolution()
    video_streams.download(desktop)
except:
    print(fc.LIGHTRED_EX+"An error occurred")
    print("Press Enter To Exit")
    input()
    exit()

done = True
print(f"{fc.LIGHTGREEN_EX}\rDownload Complete     {fc.WHITE}")

print("Saved in: ", desktop)
input()
