'''
note: pyttsx3 is a python text to speech library
where we convert a text to speech.
'''





import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello Mama! I can talk!!")

engine.runAndWait()