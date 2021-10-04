import PyPDF2
import pyttsx3





path = open(r'/Users/omar/Desktop/omar_workspace/code_for_Kids/automation_class/oldmansea.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(path)

from_page = pdfreader.getPage(1)

text = from_page.extractText()


speak = pyttsx3.init()

speak.say(text)

speak.runAndWait()

