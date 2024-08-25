import requests
import os
from pdfminer.high_level import extract_text
from playsound import playsound

API_KEY = os.environ["API_KEY"]


def text_to_speech(api_key, text, filename="output.mp3"):
    url = "http://api.voicerss.org/"
    params = {
        "key": api_key,
        "src": text,
        "hl": "en-us",
        "c": "mp3",
        "r": 10,
        'f': '44khz_16bit_stereo'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        playsound(filename)
        os.remove(filename)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


text = extract_text('pdf_to_audiobook.pdf')

# it is working with max 1500 characters
if len(text) > 1500:
    for i in range(0, len(text), 1500):
        chunk = text[i:i+1500]
        text_to_speech(API_KEY, chunk, filename=f"output_{i//1500}.mp3")
else:
    text_to_speech(API_KEY, text)


