import requests

# Запрос к статическому сайту погоды
response = requests.get("https://www.weather.kz/weather/astana")
html_content = response.text

# Извлечение погоды из HTML-кода с использованием string.split()
start_index = html_content.find('<span class="temp-max"')
end_index = html_content.find('</span>', start_index)
weather_info = html_content[start_index:end_index]
weather = weather_info.split(">")[1]

print("Погода в Астане:", weather)
