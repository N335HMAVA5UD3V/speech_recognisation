import pyttsx3
text_sp = pyttsx3.init()
text = input("enter the text")


# voice changing
voices = text_sp.getProperty('voices')
for voice in voices:
    print("ID:",voice.id)
text_sp.setProperty('voices',voices[0].id)
text_sp.say(text)
text_sp.runAndWait()