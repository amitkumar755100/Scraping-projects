
import requests

import pandas as pd
from bs4 import BeautifulSoup as BS
url="https://www.yellow-pages.ph/search/data-entry/nationwide/page-1"
r=requests.get(url)
soup=BS(r.text,"html.parser")
detail_page_data=[]
for i in soup.find_all("div","search-business"):
    links="https://www.yellow-pages.ph"+i.find("a").get("href")
    r_1=requests.get(links)
    soup_1=BS(r_1.text,"html.parser")
    try:
        image=soup_1.find("img","border").get("src")
    except:
        "none"
    try:
        tread_name=soup_1.find("h1").text.strip()
    except:
        "none"
    try:
        address=soup_1.find("a","biz-link yp-click").text.strip()
    except:
        "none"
    try:
        number=soup_1.find("span","phn-txt").text.strip()
    except:
        "none"
    try:
        email=soup_1.find("a","biz-link d-block ellipsis yp-click email-link").get("href")
    except:
        "none"
    try:
         web_side=soup_1.find("a","biz-link d-block ellipsis yp-click website-link").get("href")
    except:
        "none"
    try:
        social_media=[]
        for i in soup_1.find_all("a","biz-link d-block ellipsis yp-click social-media-link"):
            social_media.append(i.get("href"))
    except:
        "none"
    try:
        operating_hour=soup_1.find("div","icon-la b yp-green").next.next.strip()
    except:
        "none"
    try:
        about_us=soup_1.find("div","col-md-12 text-word-wrap").text.strip().replace("\n",",")
    except:
        "none"
    try:
        dict=[]
        for i in soup_1.find_all("div","row biz-day"):
            days=i.find_all("div","business_day p-1")[0]
            time=i.find_all("div","business_day p-1")[1]
            dict.update({days.text.strip():time.text.strip()})
    except:
        "none"
    try:
        rating=soup_1.find("div","rating-num").text.strip()
    except:
        "none"
    try:
        photos_link=[]
        for i in soup_1.find_all("a","photos-item open-lightGallery p-1"):
            photos_link.append(i.get("href"))
    except:
        "none"
    try:
        videos_link=[]
        for i in soup_1("a","photos-item open-lightGalleryVideo p-1"):
            videos_link.append(i.get("href"))
    except:
        "none"
    detail_page_data.append({
        "tread_image":image,
        "tread_name":tread_name,
        "address":address,
#         "phone_number":number,
        "email_id":email,
        "web_side":web_side,
        "social_media":social_media,
        "operating_hour":operating_hour,
        "about_us":about_us,
        "office_hour":dict,
        "rating":rating,
        "photo":photos_link,
        "videos_link":videos_link,

    })
# print(detail_page_data)
df=pd.DataFrame(detail_page_data)
print(df)


df.to_excel("detail_page_data.xlsx")






# import requests
# import pandas as pd
# from bs4 import BeautifulSoup as BS
# url="http://yellowpages.in/"
# r=requests.get(url)
# soup=BS(r.text,"html.parser")
# data_of_hyderabadcity=[]

# for i in soup.find("ul","homeCategoriesList"):
#     links="http://yellowpages.in/"+i.find("a").get("href")
    
# #     r_1=requests.get(links)
#     soup_1=BS(r_1.text,"html.parser")

#     for j in soup_1.find_all("div","popularTitleTextBlock"):
#         links_1="http://yellowpages.in"+j.find("a").get("href")

#         r_2=requests.get(links_1)
#         soup_2=BS(r_2.text,"html.parser")
        
#         try:
#             title=soup_2.find("h1","businessTitle").text.strip()
#         except:
#             "none"
#         try:
#             rating=soup_2.find("p","ratingBlock").find("span").get("class")[1]
#         except:
#             "none"
#         try:
#             review=soup_2.find("a","ratingCount").text.strip()
#         except:
#             "none"
#         try:
#             number=soup_2.find("a","businessContactNumber").text.strip()
#         except:
#             "none"
#         try:
#             address=soup_2.find("div","contactNumbers").text.strip()
#         except:
#             "none"
#         # try:
#         #     business_timings=soup_2.find("ul","leftColList bTimings").text.strip() 
#         # except:
#         #     "none"
                  
#         try:
#             business_timings ={}
#             for i in soup_2.find("ul",id="MainContent_ulTimings").find_all("li"):
#                 days=(i.find_all("span")[0])
#                 time=(i.find_all("span")[1])
#                 business_timings.update({days.text.strip():time.text.strip()})
#         except:
#             "none"
         
#         try:
#             our_services = soup_2.find("ul","ourServicesList").text
#         except:
#             "none"
#         try:
#             paytm=soup_2.find("div","overviewEachRow paymentMethods").text.strip()
#         except:
#             "none"
#         try:
#             ourServicesList =[]
#             for x in soup_2.find_all("ul","ourServicesList")[3]:
#                 ourServicesList.append(i.find("a").get("href"))
#         except:
#             "none"
#         data_of_hyderabadcity.append({
#             "title":title,
#             "rating":rating,
#             "review":review,
#             "number":number,
#             "address":address,
#             "buiness_timing":business_timings,
#             "our_services":our_services,
#             "paytm":paytm,
#             "ourserviceslist":our_services,

#         })
#         print(data_of_hyderabadcity)
#         df=pd.DataFrame(data_of_hyderabadcity                                                                                                                                                                                                                                                                                                   )
#         print(df)
#         df.to_excel("data_hyderabad.xlsx")
    











    
            





 