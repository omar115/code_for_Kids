
from google_trans_new import google_translator      #importing the google translator library

translator = google_translator()    #initializing the google translator library


#how to translate one language to another language
output_text = translator.translate('হ্যালো',lang_tgt='en')   #lang_tgt == target language

print(output_text)

#how to detect a language

detector = translator.detect('হ্যালো')
print(detector)

#how to pronounce a language
pronounce = translator.translate('হ্যালো', lang_src='bn', lang_tgt='en', pronounce=True)
print(pronounce)
