from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.tokopedia.com/search?st=&q=laptop&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='

driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
data = []
for i in range(17):
    for item in soup.findAll('div', class_ = 'css-5wh65g'):
        nama_produk = item.find('div', class_ = 'VKNwBTYQmj8+cxNrCQBD6g==')
        if not nama_produk: break
        harga_produk = item.find('div', class_ = '_8cR53N0JqdRc+mQCckhS0g==')
        rating = item.find('span', class_ = 'nBBbPk9MrELbIUbobepKbQ==')
        terjual = item.find('span', class_ = 'eLOomHl6J3IWAcdRU8M08A==')
        toko = item.find('span', class_ = 'X6c-fdwuofj6zGvLKVUaNQ== -9tiTbQgmU1vCjykywQqvA== flip')
        alamat_toko = item.find('span', class_ = '-9tiTbQgmU1vCjykywQqvA== flip')
    
        data.append(
            (nama_produk, harga_produk, rating, terjual, toko, alamat_toko)
        )
    driver.execute_script('window.scrollBy(0, 250)')
    time.sleep(1)

driver.close()

df = pd.DataFrame(data, columns= ["nama_produk", "harga_produk", "rating", "terjual", "toko", "alamat_toko"])
all_data = df.dropna(how='any')
print(all_data)
