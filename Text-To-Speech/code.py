from gtts import gTTS
import os
language="en"
while True:
    text=input("Give any text to speak:")
    obj=gTTS(text=text,lang=language,slow=False)
    obj.save("output.mp3")
    os.system("start output.mp3")
