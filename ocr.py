import ocrspace
import requests
from pprint import pprint


apikey='K89677753388957'

api = ocrspace.API()
# Or if you have a custom API host, API key or desired language, pass those:
# api = ocrspace.API(endpoint='https://api.ocr.space/parse/image', api_key='apikey')
#
#
# api.ocr_url('URL of image goes here')
#
#
# api.ocr_file('image.jpg')
# # or:
# api.ocr_file(open('image.jpg', 'rb'))  # or any other file pointer

# https://api.ocr.space/parse/imageurl?apikey=K89677753388957&url=http://i.imgur.com/fwxooMv.png

# response= requests.get('https://api.ocr.space/parse/imageurl?apikey=K89677753388957&url=http://i.imgur.com/fwxooMv.png')
# print(response.json())
# print(response)
data = ''

def ocr_space_file(filename, overlay=False, api_key=apikey, language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


test_file = ocr_space_file(filename='bukti transfer/resi (16).png')
bersih= test_file.strip()
pprint(bersih)
data=bersih
try:

    rp = data.index('Rp')
    print(data)
    print(rp)
    print(data[rp:rp+9])
except:
    rp = data.index('IDR')
    cleaning = data[rp:]
    print(cleaning)
    last = cleaning.index('\\r')
    print(cleaning[:last])

