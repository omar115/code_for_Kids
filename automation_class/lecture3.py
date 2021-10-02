import PyPDF2
import pyttsx3
from pyttsx3 import engine

# step 1: to read the pdf

path = open(r'/Users/omar/Desktop/omar_workspace/code_for_Kids/automation_class/oldmansea.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(path)

# step 2: select a page and extract string from that page

page = pdfreader.getPage(1)

text = page.extractText()

print(text)

# step 3: use python text to speech library
# and read the text, convert to audio speech

engine = pyttsx3.init()

engine.say(text)

engine.runAndWait()