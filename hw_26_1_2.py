import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.weather.kz/weather/astana")
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
weather_info = soup.find("span", class_="temp-max").get_text()

print("Погода в Астане:", weather_info)
