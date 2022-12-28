from googletrans import Translator, constants
from pprint import pprint

data = 'تمہارا نام کیا ہے'

# init the Google API translator
translator = Translator()
# translate a spanish text to english text (by default)
translation = translator.translate(data)
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
print(translation.text)