
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
url="https://www.yellow-pages.ph/search/warehouse/nationwide/page"
def crawl_list_page(url):
    r=requests.get(url)
    # print(r)
    soup= BS(r.text,"html.parser")
    listing=soup.find_all("div","search-listing")
    products=[]
    for i in listing:
        try:
          title=i.find("h2","search-tradename").text.strip()
        except:
          title="not available"
          print(title)
        try:
           product_url="https://www.yellow-pages.ph"+i.find("a").get("href")
        except:
          product_url="not available"
        try:
          address=i.find("div","search-busines-address").text.strip()
        except:
           address="not available"
        try:
          phone_number=i.find("a",attrs={"data-section":"contact number"}).get("data-phone")    
        except:
          phone_number="not available"
        products.append({
            "title":title,
            "product_url":product_url,
            "address":address,
            "phone":phone_number,
              })
    return products
    # print(products)

    # df=pd.DataFrame(products)
    # print(df)
    # df.to.excel("products.xlsx")  

   

# # url="https://www.yellow-pages.ph/search/data-entry/nationwide/page-2"
# # # df=pd.DataFrame(products)
# # print(df)
# # df.to.excel("products.xlsx")  









    
  
 

  