from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

def get_currency_exchange_rate():
    driver.get("URL_сайта_погоды")
    currency_rate_element = driver.find_element_by_css_selector("селектор_для_курса_валюты")
    currency_rate = currency_rate_element.text
    return currency_rate

def get_prices_from_marketplace():
    driver.get("URL_маркетплейса")
    
    price_elements = driver.find_elements_by_css_selector("селектор_для_цен")
    prices = [element.text for element in price_elements]
    return prices

currency_exchange_rate = get_currency_exchange_rate()
print("Курс валюты:", currency_exchange_rate)

marketplace_prices = get_prices_from_marketplace()
print("Цены на маркетплейсе:", marketplace_prices)

driver.quit()
