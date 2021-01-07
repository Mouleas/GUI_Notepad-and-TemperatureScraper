import requests
from bs4 import BeautifulSoup

def weather(place):
    url = f"http://www.google.com/search?&q=weather in {place}"
    r = requests.get(url)
    s = BeautifulSoup(r.text,'html.parser')
    temp = s.find("div",class_="BNeawe" ).text
    return temp

if __name__ == "__main__":
    place = str(input())
    print(f"Current temperature in {place} : {weather(place)} ")  
