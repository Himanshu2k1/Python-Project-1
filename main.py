import requests
import json


url = "https://newsapi.org/v2/top-headlines?country=" \
      "in&category=technology&apiKey=ead513cbfeff4ff39edc6c82a562b673"


def speak(string):
    from win32com.client import Dispatch
    speech = Dispatch("SAPI.SpVoice")
    speech.Speak(string)


news = requests.get(url).text
news_json = json.loads(news)
news_list = news_json["articles"]
for article in news_list:
    speak(article["title"])
