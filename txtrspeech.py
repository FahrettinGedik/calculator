from gtts import gTTS
import os

myText = "Adem madene gitmis adem madende badem yemis madem Adem madende badem yemis, neden bize getirmemis."

language = 'tr'

outputr = gTTS(text=myText, lang=language, slow=False)

outputr.save("outputr.mp3")

os.system("start outputr.mp3")