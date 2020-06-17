from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import pdfkit as pdf


driver = webdriver.Chrome()
products=[] #List to store name of the product
prices=[] #List to store price of the product
#ratings=[]

driver.get("https://www.flipkart.com/search?q=gaming+laptops+under+75000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_2_15_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_2_15_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=gaming+laptops+under+75000&requestId=286ec596-9538-4724-8b84-1a233e6006a2")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
for div in soup.findAll('div', attrs={'class':'_3liAhj'}):
    name = div.find('a',href=True, attrs={'class':'_2cLu-l'}).text
    price = div.find('div', attrs={'class':'_1vC4OE'}).text
    #rating = div.find('div', attrs={'class':'hGSR34'}).text
    
    products.append(name)
    prices.append(price)
    #ratings.append(rating)
    
    
df = pd.DataFrame({'Product Name':products, 'Price':prices}) 
df.to_csv('laptops under 75K.csv', index=False, encoding='utf-8')

csv_file = 'laptops under 75K.csv'
html_file = csv_file[:-3]+'html'
pdf_file = csv_file[:-3]+'pdf'

df = pd.read_csv(csv_file, sep=',')
df.to_html(html_file)
