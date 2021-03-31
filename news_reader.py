import json
import requests

def speak(string):
    from win32com.client import Dispatch
    speech = Dispatch("SAPI.SpVoice")
    speech.Speak(string)

url = "https://newsapi.org" \
"/v2/top-headlines?country=in&category=technology&apiKey=ead513cbfeff4ff39edc6c82a562b673"

i = 1
news = requests.get(url).text
news_json = json.loads(news)
news_list = news_json["articles"]
for article in news_list:
    if i == 1:
        speak("Today's Headlines are : ")
    elif i > 1 and i <= 20:
        speak(f"Moving on to headline {i}")
    speak(article["title"])
    if i == 20:
        speak("That is all for today's headlines, Thank you")
    i = i + 1
