# # import requests
# # from bs4 import BeautifulSoup as BS
# # import json
# # list=[]


# # cookies = {
# #     'AMCV_43C357DF589484E40A495D80%40AdobeOrg': '179643557%7CMCIDTS%7C19923%7CMCMID%7C64509220795059661381762954870350209710%7CMCAAMLH-1721885158%7C12%7CMCAAMB-1721885158%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721287558s%7CNONE%7CvVersion%7C5.5.0',
# #     '_gcl_aw': 'GCL.1721280446.CjwKCAjw1920BhA3EiwAJT3lSVFyAddITBr-DTO91eq-Zd02_0h9HZClez_vteqG6aefqFFZ7RNoZxoCylMQAvD_BwE',
# #     '_gcl_gs': '2.1.k1$i1721280441',
# #     '_gcl_au': '1.1.383352149.1721280358',
# #     'AMCVS_43C357DF589484E40A495D80%40AdobeOrg': '1',
# #     '_ga_MGJJ293S48': 'GS1.1.1721280358.1.1.1721280448.52.0.0',
# #     '_ga': 'GA1.1.1718027596.1721280358',
# #     '_ga_R8B3JV8BYF': 'GS1.1.1721280358.1.1.1721280446.0.0.0',
# #     '_ga_Q3470S4J87': 'GS1.1.1721280358.1.1.1721280445.56.0.0',
# #     '_ga_D148XMNPGZ': 'GS1.1.1721280359.1.1.1721280448.0.0.0',
# #     '_gid': 'GA1.2.1696109630.1721280359',
# #     '_gac_UA-5956906-1': '1.1721280359.CjwKCAjw1920BhA3EiwAJT3lSVFyAddITBr-DTO91eq-Zd02_0h9HZClez_vteqG6aefqFFZ7RNoZxoCylMQAvD_BwE',
# #     '_fbp': 'fb.1.1721280359690.481602869572651252',
# #     'localCurrency': 'INR',
# #     'gpv_pn': 'fnp%20ind%3Aplp%3Aindia',
# #     's_cc': 'true',
# #     'cto_bundle': 'GX3UiV9LWW1odmg3cFp2eFlKRE9VR1p5MyUyRnlySkFSa1dtdGxkS2VzYTFmeVlkQzJad3ZvVjVIYWJxN25TRzZvOHlkVTZkMWdHaE9xNFlPUGNEWnl6dWN6UXF3YnB3a2g3ckgydkVITXpYU0FEb29kTVRpMXhneGUxZDhOT2c2UHozYzNEYXBUbzdra0d0ZHI5eEZTMDJvMEh2ZyUzRCUzRA',
# #     'source': 'https://www.fnp.com/?utm_source=Google&utm_medium=cpc&utm_campaign=21150229676&utm_adgroup=160562238156&utm_keyword=fnp&utm_device=c&utm_placement=&utm_network=g&gad_source=1&gclid=CjwKCAjw1920BhA3EiwAJT3lSVFyAddITBr-DTO91eq-Zd02_0h9HZClez_vteqG6aefqFFZ7RNoZxoCylMQAvD_BwE',
# #     'utm_source': 'Google',
# #     'utm_campaign': '21150229676',
# #     'utm_medium': 'cpc',
# #     'utm_content': 'undefined',
# #     'admitad_uid': 'undefined',
# #     'AMO-tid': '1652808199',
# #     'usid': '10113412',
# #     '_hjSessionUser_451981': 'eyJpZCI6ImE1YWU2MmIyLTY5MGQtNWFmNC1hZmU1LWQzMTZhOTVhMzBjMyIsImNyZWF0ZWQiOjE3MjEyODAzNjUwMDMsImV4aXN0aW5nIjp0cnVlfQ==',
# #     '_hjSession_451981': 'eyJpZCI6Ijc2YWY4OGZjLTAxODctNGFlYi04ZjZjLTNkMmQzYjliYWMxZiIsImMiOjE3MjEyODAzNjUwMDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
# #     '_uetsid': '3aadf80044c611efaef1514eb34e7ba7',
# #     '_uetvid': '3aadfcf044c611efbd651f4d13229c63',
# #     's_sq': '%5B%5BB%5D%5D',
# # }

# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
# #     'Accept': 'application/json, text/plain, */*',
# #     'Accept-Language': 'en',
# #     # 'Accept-Encoding': 'gzip, deflate, br, zstd',
# #     'x-device-type': 'desktop',
# #     'x-domain': 'www.fnp.com',
# #     'Origin': 'https://www.fnp.com',
# #     'Connection': 'keep-alive',
# #     'Referer': 'https://www.fnp.com/',
# #     # 'Cookie': 'AMCV_43C357DF589484E40A495D80%40AdobeOrg=179643557%7CMCIDTS%7C19923%7CMCMID%7C64509220795059661381762954870350209710%7CMCAAMLH-1721885158%7C12%7CMCAAMB-1721885158%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721287558s%7CNONE%7CvVersion%7C5.5.0; _gcl_aw=GCL.1721280446.CjwKCAjw1920BhA3EiwAJT3lSVFyAddITBr-DTO91eq-Zd02_0h9HZClez_vteqG6aefqFFZ7RNoZxoCylMQAvD_BwE; _gcl_gs=2.1.k1$i1721280441; _gcl_au=1.1.383352149.1721280358; AMCVS_43C357DF589484E40A495D80%40AdobeOrg=1; _ga_MGJJ293S48=GS1.1.1721280358.1.1.1721280448.52.0.0; _ga=GA1.1.1718027596.1721280358; _ga_R8B3JV8BYF=GS1.1.1721280358.1.1.1721280446.0.0.0; _ga_Q3470S4J87=GS1.1.1721280358.1.1.1721280445.56.0.0; _ga_D148XMNPGZ=GS1.1.1721280359.1.1.1721280448.0.0.0; _gid=GA1.2.1696109630.1721280359; _gac_UA-5956906-1=1.1721280359.CjwKCAjw1920BhA3EiwAJT3lSVFyAddITBr-DTO91eq-Zd02_0h9HZClez_vteqG6aefqFFZ7RNoZxoCylMQAvD_BwE; _fbp=fb.1.1721280359690.481602869572651252; localCurrency=INR; gpv_pn=fnp%20ind%3Aplp%3Aindia; s_cc=true; cto_bundle=GX3UiV9LWW1odmg3cFp2eFlKRE9VR1p5MyUyRnlySkFSa1dtdGxkS2VzYTFmeVlkQzJad3ZvVjVIYWJxN25TRzZvOHlkVTZkMWdHaE9xNFlPUGNEWnl6dWN6UXF3YnB3a2g3ckgydkVITXpYU0FEb29kTVRpMXhneGUxZDhOT2c2UHozYzNEYXBUbzdra0d0ZHI5eEZTMDJvMEh2ZyUzRCUzRA; source=https://www.fnp.com/?utm_source=Google&utm_medium=cpc&utm_campaign=21150229676&utm_adgroup=160562238156&utm_keyword=fnp&utm_device=c&utm_placement=&utm_network=g&gad_source=1&gclid=CjwKCAjw1920BhA3EiwAJT3lSVFyAddITBr-DTO91eq-Zd02_0h9HZClez_vteqG6aefqFFZ7RNoZxoCylMQAvD_BwE; utm_source=Google; utm_campaign=21150229676; utm_medium=cpc; utm_content=undefined; admitad_uid=undefined; AMO-tid=1652808199; usid=10113412; _hjSessionUser_451981=eyJpZCI6ImE1YWU2MmIyLTY5MGQtNWFmNC1hZmU1LWQzMTZhOTVhMzBjMyIsImNyZWF0ZWQiOjE3MjEyODAzNjUwMDMsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_451981=eyJpZCI6Ijc2YWY4OGZjLTAxODctNGFlYi04ZjZjLTNkMmQzYjliYWMxZiIsImMiOjE3MjEyODAzNjUwMDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _uetsid=3aadf80044c611efaef1514eb34e7ba7; _uetvid=3aadfcf044c611efbd651f4d13229c63; s_sq=%5B%5BB%5D%5D',
# #     'Sec-Fetch-Dest': 'empty',
# #     'Sec-Fetch-Mode': 'cors',
# #     'Sec-Fetch-Site': 'same-site',
# #     # Requests doesn't support trailers
# #     # 'TE': 'trailers',
# # }

# # params = {
# #     'currency': 'INR',
# #     'geoId': 'india',
# #     'isFacetEnabled': 'true',
# #     'page': '1',
# #     'size': '36',
# #     'categoryUrl': 'fnp.com/flowers-lp',
# #     'domainId': 'fnp.com',
# #     'lang': 'en',
# #     'isOnScroll': 'true',
# # }

# # response = requests.get('https://atcdel.fnp.com/columbus/v1/productList', params=params, cookies=cookies, headers=headers)
# # # print(response)
# # def fnp():
# #     js=response.json()["data"]

# #     for i in js:
# # #         name=i["productName"]
# # #         price=i["price"].get("mrp")
# # #         # ratingvalue=i["rating"].get("ratingCount")
# # #         images=i["productImage"].get("path")
# # #         list.append({"name":name,"price":price,"images":images})
# # #         print(list)
# # # #         detail_page(list)


# # # # def detail_page(meta):
# # # fnp()
       
    







# import requests
# import json
# from requests import session
# from bs4 import BeautifulSoup as BS
# s = session()
# import pandas as pd 

# import requests

# cookies = {
#     'AMCV_43C357DF589484E40A495D80%40AdobeOrg': '179643557%7CMCIDTS%7C19921%7CMCMID%7C13772715915626693603499164050766485717%7CMCAAMLH-1720848294%7C12%7CMCAAMB-1721108797%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721118679s%7CNONE%7CvVersion%7C5.5.0',
#     '_gcl_au': '1.1.2002253386.1720243495',
#     '_ga_MGJJ293S48': 'GS1.1.1720253644.4.0.1720253644.60.0.0',
#     '_ga': 'GA1.2.1701179637.1720243496',
#     '_ga_Q3470S4J87': 'GS1.1.1720253644.4.0.1720253644.60.0.0',
#     '_ga_D148XMNPGZ': 'GS1.1.1720253644.4.0.1720253644.0.0.0',
#     '_ga_R8B3JV8BYF': 'GS1.1.1720253644.4.1.1720253644.0.0.0',
#     '_fbp': 'fb.1.1720243496162.73653348586873234',
#     'cto_bundle': 'Jivd2l9FS3M2cVk3a0FRVngzUG9TWkFxUjA4aCUyRmNUa2tIV0FMQzljVFNCTTFSVTZqRXZnaDJ3eGdrdUdXcktUNGdXa0FIZ3BCQ3BXZEY5UjJoQXZQc0daYldPdjg2SGxtclFWa0UxWSUyQjc5RUFJZWNNb2xFcFY5RFE4eVk4MXlhRVV2UnVsazVzU1hXQ2I1MktJZmolMkI2V1NCYVElM0QlM0Q',
#     '_hjSessionUser_451981': 'eyJpZCI6ImU1NTQzMzljLTNjNjQtNWFmMC04YWFlLTgyYTBiYjUzMjIzOSIsImNyZWF0ZWQiOjE3MjAyNDM1MDA2MDcsImV4aXN0aW5nIjp0cnVlfQ==',
#     '_uetvid': '16c1e8f03b5811efa1c98b8482c5e210',
#     'AMCVS_43C357DF589484E40A495D80%40AdobeOrg': '1',
#     'localCurrency': 'INR',
#     'language-preference': 'en',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
#     'Accept': 'application/json, text/plain, /',
#     'Accept-Language': 'en',
#     # 'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'x-device-type': 'desktop',
#     'x-domain': 'www.fnp.com',
#     'Origin': 'https://www.fnp.com',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.fnp.com/',
#     # 'Cookie': 'AMCV_43C357DF589484E40A495D80%40AdobeOrg=179643557%7CMCIDTS%7C19921%7CMCMID%7C13772715915626693603499164050766485717%7CMCAAMLH-1720848294%7C12%7CMCAAMB-1721108797%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721118679s%7CNONE%7CvVersion%7C5.5.0; _gcl_au=1.1.2002253386.1720243495; _ga_MGJJ293S48=GS1.1.1720253644.4.0.1720253644.60.0.0; _ga=GA1.2.1701179637.1720243496; _ga_Q3470S4J87=GS1.1.1720253644.4.0.1720253644.60.0.0; _ga_D148XMNPGZ=GS1.1.1720253644.4.0.1720253644.0.0.0; _ga_R8B3JV8BYF=GS1.1.1720253644.4.1.1720253644.0.0.0; _fbp=fb.1.1720243496162.73653348586873234; cto_bundle=Jivd2l9FS3M2cVk3a0FRVngzUG9TWkFxUjA4aCUyRmNUa2tIV0FMQzljVFNCTTFSVTZqRXZnaDJ3eGdrdUdXcktUNGdXa0FIZ3BCQ3BXZEY5UjJoQXZQc0daYldPdjg2SGxtclFWa0UxWSUyQjc5RUFJZWNNb2xFcFY5RFE4eVk4MXlhRVV2UnVsazVzU1hXQ2I1MktJZmolMkI2V1NCYVElM0QlM0Q; _hjSessionUser_451981=eyJpZCI6ImU1NTQzMzljLTNjNjQtNWFmMC04YWFlLTgyYTBiYjUzMjIzOSIsImNyZWF0ZWQiOjE3MjAyNDM1MDA2MDcsImV4aXN0aW5nIjp0cnVlfQ==; _uetvid=16c1e8f03b5811efa1c98b8482c5e210; AMCVS_43C357DF589484E40A495D80%40AdobeOrg=1; localCurrency=INR; language-preference=en',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
# }



# response = requests.get('https://atcdel.fnp.com/columbus/v1/productList', cookies=cookies, headers=headers)




# s.headers.update(headers)
# search_input = str(input("search_input --"))

# def fnp ():
#     list_1 = []
#     page = 0
#     while True:
#         params = {
#         'currency': 'INR',
#         'geoId': 'india',
#         'isFacetEnabled': 'true',
#         'page': f'{page}',
#         'size': '36',
#         'categoryUrl': f'fnp.com/{search_input}-lp',
#         'domainId': 'fnp.com',
#         'lang': 'en',
#         'isOnScroll': 'true',
#         }
#         response = requests.get('https://atcdel.fnp.com/columbus/v1/productList', params=params, cookies=cookies, headers=headers)

#         js = response.json()
#         if js["totalPages"]:
#             total_page = js["totalPages"]
        
#         if page == int(total_page):
#                 break
#         else:
#             page+=1
#         js = (response.json())["data"]
#         for x in js:
#             product_url = "https://www.fnp.com" + x.get('productUrl')
#             # print(product_url)
#             list_1.append(product_url)
#             detail_page(product_url)
#     return list_1

# def detail_page(meta):

#     response = s.get(meta)
#     soup = BS (response.text,"html.parser")
#     list_1 = []
#     product_data = []
#     # print(soup)
#     try:
#         name = soup.find("h1","price-with-name-desktop_productName__3kv8O").text
#     except:
#         name = None
#     try:
#         price = soup.find("span","odometer odometer-auto-theme").text
#     except:
#         price = None
#     try:
#         rating = soup.find("span","product-card_rating-sec__34VZH").text
#     except:
#         rating = None
#     try:
#         for x in soup.find("div","product-desc-desktop_descriptionTitle__2Q-Ha").find_all("li")[0:9]:
#             product_details = x.text
#             list_1.append(product_details)
#     except:
#         product_details = None
#     try:   
#         img_tag = soup.find("img",id="original-image")
#         image = "https://www.fnp.com" + img_tag.get("src")
#     except:
#         image = None
#     # try:
#     #     description = soup.find("div","product-desc-desktop_descriptionTitle__2Q-Ha").text
#     # except:
#     #     description = None
    
#     product_data.append({

#         "name":name,
#         "price":price,
#         "rating":rating,
#         "product_detail":product_details,
#         "image":image,
#         # "description":description
#     })
#     print(product_data)


# # df=pd.DataFrame("product_data")
# # print(df)
# # df.to_excel("product_data.xlsx")
# fnp()




























# import requests
# from bs4 import  BeautifulSoup as BS
# from requests import session
# from lxml import html
# import json




















import requests
from requests import Session
from bs4 import BeautifulSoup as BS
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
}

s = Session()
s.headers.update(headers)

search_input = input("search_input -- ")

def fnp():
    product_data = []  # Collect all details here
    list_1 = []  # Collect URLs if needed

    params = {
        'currency': 'INR',
        'geoId': 'india',
        'isFacetEnabled': 'true',
        'size': '36',
        'categoryUrl': f'fnp.com/{search_input}-lp',
        'domainId': 'fnp.com',
        'lang': 'en',
        'isOnScroll': 'true',
    }

    # Fetch page 0 to get total_pages
    params['page'] = '0'
    response = requests.get('https://atcdel.fnp.com/columbus/v1/productList', params=params, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching initial page: {response.status_code}")
        return list_1
    
    js = response.json()
    total_pages = js.get('totalPages', 0)
    print(f"Total pages found: {total_pages}")

    for page in range(total_pages):
        if page > 0:
            params['page'] = str(page)
            response = requests.get('https://atcdel.fnp.com/columbus/v1/productList', params=params, headers=headers)
            if response.status_code != 200:
                print(f"Error fetching page {page}: {response.status_code}")
                continue
            js = response.json()
        
        data = js.get('data', [])
        for x in data:
            product_url = "https://www.fnp.com" + x.get('productUrl', '')
            list_1.append(product_url)
            details = detail_page(product_url)
            if details:
                product_data.append(details)
    
    # Save to Excel
    if product_data:
        df = pd.DataFrame(product_data)
        df.to_excel("product_data.xlsx", index=False)
        print("Data saved to product_data.xlsx")
    else:
        print("No data collected.")
    
    return list_1

def detail_page(url):
    response = s.get(url)
    if response.status_code != 200:
        print(f"Error fetching detail page {url}: {response.status_code}")
        return None
    
    soup = BS(response.text, "html.parser")
    
    try:
        name = soup.find("h1", class_="price-with-name-desktop_productName__3kv8O").text.strip()
    except:
        name = None
    
    try:
        price = soup.find("span", class_="odometer odometer-auto-theme").text.strip()
    except:
        price = None
    
    try:
        rating = soup.find("span", class_="product-card_rating-sec__34VZH").text.strip()
    except:
        rating = None
    
    product_details = []
    try:
        desc_div = soup.find("div", class_="product-desc-desktop_descriptionTitle__2Q-Ha")
        if desc_div:
            for li in desc_div.find_all("li")[:9]:
                product_details.append(li.text.strip())
    except:
        product_details = []
    
    try:
        img_tag = soup.find("img", id="original-image")
        image = "https://www.fnp.com" + img_tag.get("src") if img_tag else None
    except:
        image = None
    
    return {
        "name": name,
        "price": price,
        "rating": rating,
        "product_detail": ", ".join(product_details),
        "image": image,
    }

fnp()