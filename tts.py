# Use command for os.system based on your os

from gtts import gTTS
import os

text = 'Hi there! I am Sanya. Nice to meet you'
language = 'en'

obj = gTTS(text=text, lang=language, slow=False)
obj.save('intro.mp3')
os.system('mpg123 intro.mp3')
