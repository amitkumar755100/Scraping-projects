# import requests 
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# print(r.status_code)

# import requests
# from bs4 import BeautifulSoup as BS
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# if(r.status_code==200):
#     soup = BS(r.content,"html.parser")
#     companyNames=[]
#     outer_block=soup.find_all("div",class_="search-listing")
#     for block in outer_block:
#          company_name=block.find("h3",class_="tradename")
#          if(company_name!=None):
#         #  companyNames.append(company_name)
#         #  companyNames.append(company_name)
#            print(company_name.text)
# else:
#      ("site is not responding")

     

# import requests
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# print(r.status_code)


# import requests
# from bs4 import BeautifulSoup as bs
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# if(r.status_code==200):
#     soup=bs(r.content,"html.parser")
#    #  companyaddresses=[]
#     outer_block=soup.find_all("div","search-listing")
#    #  breakpoint()
#     for block in outer_block:
#          company_addresse=block.find("div","search-busines-address")
#          if company_addresse != None:
#             print(company_addresse.text)
      


#          # companyaddresses.append(company_addresse)
#       #   print(company_addresse)
# else:
#         print("not a responding")

    

# import requests
# url="https://www.yellow-pages.ph/search/builders/nationwide/page-1"
# # r=requests.get(url)
# print(r.status_code)

# import requests
# from bs4 import BeautifulSoup as BS
# url="https://www.yellow-pages.ph/search/builders/nationwide/page-1"
# r=requests.get(url)
# if(r.status_code==200):
#     soup=BS(r.content,"html.parser")
# #     print(soup.title.get_text())
# html=soup.find_all("div",class_="rating-num")
# # print(html)
# for item in html:
#     name=item.find("a",class_="yp-click")
#     print(name)


# import requests
# url="https://www.yellow-pages.ph/business/rivera-sarvida-construction-incorporated"
# r=requests.get(url)
# print(r.status_code)

# import requests
# from bs4 import BeautifulSoup as bs
# url="https://www.yellow-pages.ph/business/rivera-sarvida-construction-incorporated"
# r=requests.get(url)
# if(r.status_code==200):
#     soup=bs(r.content,"html.parser")
#     companyphonenumbers=[]
#     outer_block=soup.find_all("span","phn-txt")
#    #  breakpoint()
#     for block in outer_block:
#        company_phone=block.find("span","phn-txt")
#          # if company_phone != None:
# companyphonenumbers.append(company_phone)
# print(company_phone.text)


# import requests
# from bs4 import BeautifulSoup as BS
# url = "https://www.yellow-pages.ph/business/lcsn-express-movers-incorporated"
# r = requests.get(url)
# if(r.status_code == 200):
#     soup = BS(r.content,'html.parser')
#     companyNames = []
#     outer_block = soup.find_all("div","search-listing  ")
#     for block in outer_block:
#         company_name = block.find("h1","h1-tradename")
#         if(company_name!=None):
#         companyNames.append(company_name)
#         print(companyNames) #list of company names
# # else:
# #     print("site is not responding")







# import requests
# from bs4 import BeautifulSoup
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# # print(r)
# soup=BeautifulSoup(r.text,"lxml")

# # print(soup)
# name=soup.find_all("h2",class_="search-tradename")
# for i in name:

# #  print(i.text)

# import requests
# from bs4 import BeautifulSoup
# url="https://www.yellow-pages.ph/business/lcsn-express-movers-incorporated"
# r=requests.get(url)
# soup=BeautifulSoup(r.text,"lxml")
# phone_number=soup.find_all("span",class_="phn-txt")
# for i in phone_number:
#     print(i.text)



# import requests
# from bs4 import BeautifulSoup
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# soup=BeautifulSoup(r.text,"html")
# heading=soup.find_all("h3",class_="search-businessname")
# for i in heading:
#     print(i.text)





# a={"address":"","heading":""}
# import requests
# from bs4 import BeautifulSoup as BS
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url)
# # print(r)
# soup=BS(r.text,"lxml")
# media_all=[]
  
# for media in media:
#     media_all.append(media)
#     print(media.text)


# import requests
# from bs4 import BeautifulSoup as BS


# url = "https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"




# def crawl_list_page(url):
#     r = requests.get(url)
#     soup = BS(r.text,'html.parser')
#     listing = soup.find_all('div','search-listing')
#     products = []
#     for i in listing:
#         title = i.find('h2')
#         if title:
#             title = title.text.strip()
#         else:
#             title = "Not Available"
#         try:
#             product_url = 'https://www.yellow-pages.ph'+i.find('a').get('href')
#         except:
#             product_url = "Not Available"

#         try:
#             address = i.find('div','search-busines-address').text.strip()
#         except:
#             address = "Not Available"
#         try:
#             timing = i.find('div','search-busines-time').text.strip()
#         except:
#             timing = "Not Available"

#         try:
#             phone_number = i.find('a',attrs={'data-section':'contact number'}).get('data-phone')
#         except:
#             phone_number = "Not Available"
#         products.append({
#             'title':title,
#             'product_url':product_url,
#             'address':address,
#             'timing':timing,
#             'phone':phone_number
#         })
#     return products
# # print(products)


# url = "https://www.yellow-pages.ph/search/data-e ntry/nationwide/page-1"
# for i in url:
#    products = crawl_list_page(url)
# print(products)





import requests
from bs4 import BeautifulSoup as BS
url="https://www.yellow-pages.ph/business/coffeebot-solutions"
r=requests.get(url)
soup1=BS(r.text,"html.parser")
listing=soup1.find_all("div","col-sm-12 col-lg-8 p-0 pl-xl-3")
detail_of_page=[]
for i in listing:

# for i in soup1.find_all("div","search-business"):
    links="https://www.yellow-pages.ph"+i.find("a").get("href")

    r_2 = requests.get(links)

    soup2 = BS(r_2.text,("html.parser"))
  
    try:
        title=soup2.find("h1","h1-single-businessname").text.strip()
    except:
        "n"
    try:
        website_tag=soup2.find("span","capsule-rounded").text.strip()
    except:
        "n"
    try:
        image=soup2.find("img").get("src")
    except:
        "n"
    try:
        rating=soup2.find("div",class_="business-rating rating-container d-flex align-items-center biz-rating-summary").text.strip()
    except:
        "n"
    try:
        address=soup2.find("a","biz-link yp-click").text.strip()
    except:
        "n"
    try:
        phone_number=soup2.find("span","phn-txt").text.strip()
    except:
          "n"
    try:
        email=soup2.find("a","biz-link d-block ellipsis yp-click email-link").text.strip()
    except:
        "n"
    try:
        website=soup2.find("a","biz-link d-block ellipsis yp-click website-link").text.strip()
    except:
        "n"
    try:
       social_media_1=soup2.find("a",class_="biz-link d-block ellipsis yp-click social-media-link").text.strip()
    except:
        "n"
    try:
        timing=soup2.find("div","icon-la b yp-green").text.strip()
    except:
         "n"
         
    try:
        discription=soup2.find("div","col-md-12 text-word-wrap").text.strip()
    except:
        "n"

    detail_of_page.append({

        "titile":title,

        "website":website_tag,

        "image":image,

        "rating":rating,

        "address":address,

        "phone_number":phone_number,

        "email":email,

        "website":website,

        "social_m":social_media_1,

        # "timing":timing,

        "discription":discription,
        
    })
    # print(detail_of_page)
    print(timing)
   
    
# print(links)
