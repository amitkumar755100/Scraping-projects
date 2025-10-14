

import requests
import re

url="https://www.flipkart.com/search?q=iphone+13&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+13%7CMobiles&requestId=9910e83c-0828-49dd-bc37-b6f4c3410dee&as-searchtext=ip"

response=requests.get(url)

links=re.findall('noopener noreferrer" href="(.*?)"',response.text)
for i in links:
    l=("https://www.flipkart.com"+i)
    data=requests.get(l)
    try:
        name=re.search('"VU-ZEz">(.*?)</span>', data.text).group(1)
    except:
        name="not available"
    try:
        image=[]

        photo=re.findall('"DByuf4 IZexXJ jLEJ7H"(.*?)</div>',data.text)
        for i in photo:
            image.append(re.search('src="(.*)' ,i).group(1))
    except:
        image="not available image"
    
    try:
        price=re.search('"Nx9bqj CxhGGd">(.*?)</div>',data.text).group(1)
    except:
        price="not available"
    try:
        comment=re.search('ZmyHeo"><div><div class="">(.*?)</div><span',data.text)
    except:
        comment="not available"
    print(comment)
    try:
        ratings=re.search('"Wphh3N">(.*?)</span>',response.text).group(1).strip().replace("<span><span>","")
    except:
        ratings=""
    # print(ratings)
          

        
    
    # ratings=re.search('"Wphh3N">(.*?)</span>',data.text)
    # print(ratings)
    # except=""
    
