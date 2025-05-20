import requests
from bs4 import BeautifulSoup
import csv

url = "https://webscraper.io/test-sites/e-commerce/allinone"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="thumbnail")

data = []
for product in products:
    title = product.find("a", class_="title").text.strip()
    price = product.find("h4", class_="price").text.strip()
    data.append([title, price])

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Title", "Price"])
    writer.writerows(data)

print("Product details scraped and saved to products.csv")