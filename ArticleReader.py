import pyttsx3  # version 2.7
import requests
from bs4 import BeautifulSoup

url = "https://medium.com/launch-by-adobe/client-side-help-for-gdpr-79e1cbcfc3c2"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 175)


def content(url_input):
    res = requests.get(url_input)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = []
    res = ""
    for i in range(len(soup.select('.p'))):
        article = soup.select('.p')[i].getText().strip()
        articles.append(article)
        res = " ".join(articles)
    return res


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


contents = content(url)
# print(contents)
speak(contents)
