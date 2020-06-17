from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import pdfkit as pdf


driver = webdriver.Chrome()
products=[] #List to store name of the product
prices=[] #List to store price of the product

driver.get("https://www.flipkart.com/search?q=acer+nitro+5&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=acer+nitro+5%7CLaptops&requestId=e1372210-8b38-4dfe-9654-ea830338b8e4&as-searchtext=acer%20nitro%20")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'}).text
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'}).text
    
    products.append(name)
    prices.append(price)
    
    
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('myfile.csv', index=False, encoding='utf-8')

csv_file = 'myfile.csv'
html_file = csv_file[:-3]+'html'
pdf_file = csv_file[:-3]+'pdf'

df = pd.read_csv(csv_file, sep=',')
df.to_html(html_file)
