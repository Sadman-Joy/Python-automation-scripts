# Automation Scripts :

# Text printing
'''
text = input("Enter text to print infinitely: ")
while True:
    print(text)
'''

# copier
'''
text = input("Enter the text to print: ")
count = int(input("How many times to print it? "))

for i in range(count):
    print(text)
'''

# Remove Background from Images
'''
from rembg import remove
from PIL import Image
input = Image.open("photo.png")
output = remove(input)
output.save("photo_no_bg.png")
'''

# Download YouTube Video
'''
from pytube import YouTube

yt = YouTube("https://youtube.com/watch?v=example")
stream = yt.streams.get_highest_resolution()
stream.download()
'''

# Text-to-Speech (Voice Reader)
'''
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is your Python speaking!")
engine.runAndWait()
'''

# Generate a Random Password
'''
import random
import string

length = int(input("Enter range : "))
password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=length))
print(password)
'''