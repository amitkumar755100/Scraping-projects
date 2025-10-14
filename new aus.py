# import requests
# from bs4 import BeautifulSoup

# r=requests.get("https://www.yellow-pages.ph/search/warehouse/nationwide/page-1")
# soup=BeautifulSoup(r.content,"html.parser")

# for i in soup.find_all("div","search-listing"):
#     name=i.find("div","search-business").find("div","search-business-maininfo").h2.text
#     address=i.find("div","search-business").find("div","search-business-maininfo").h3
#     if address:
#         address=address.text
#     else:
#         None
    #  print("name","address")
    # # d={}
    # d["NAME"]=name
    # d["ADDRESS"]=address
    # print(d)
    # # l=[d,d]
    # # l.append(d)
    # # print(d)




# import requests
# from bs4 import BeautifulSoup as BS 
# url="https://www.yellow-pages.ph/search/warehouse/nationwide/page-1"
# r=requests.get(url) 
# soup=BS(r.text,"html.parser")
# listing=soup.find_all("div","search-listing")
# company_details=[]

# for i in listing:
#     phone_number=i.find("a",attrs={"data-section":"contact number"}).get("data-phone")
#     print(phone_number)
    
    # img=i.find("a").find("img").get("data-src")
    
       
   


    # service_name=i.find("div","search-capsule-container").text.strip()
  
    # rating_star=i.find("i","fas fa-star")#doubt
  
    # company_details.append({
    #     "title":title,
    #     "address":address,
    #     "service_name":service_name,
    #     "phone_number":phone_number,
    # })
 
#     

# import requests
# from bs4 import BeautifulSoup as BS
# url="https://www.yellow-pages.ph/business/coffeebot-solutions"
# r=requests.get(url)
# soup=BS(r.text,"html.parser")
# page=soup.find("div","col-sm-12 col-lg-8 p-0 pl-xl-3")
# [i.get("href") for i in page.find_all("a","biz-link d-block ellipsis yp-click social-media-link")]


    
# from requests import session
# from bs4 import BeautifulSoup as BS
# s = session()
# url = "https://www.yellowpages.com.au/"
# import pandas as pd
# data = []

# import requests

# cookies = {
#     'ak_bmsc': 'EB9FF2783882A3E92AB4B33AD9C3AB0A~000000000000000000000000000000~YAAQbRwgF3XnmlCPAQAAjBCxVheEhFcGAZXwCCNVMh+xlEcHe0S6Y2tEiAOE/jdUSR+wUojREk646IUiRflKXdvPrNINIXrdC/cHGnzqC4wYuvrYBiC2JGizN2r4/W5Iisoo0lVkyg+CX9guVk57AQiBJ7BxLQWpy/4Yqmqtum8JKb/NWz4OgT3bQfEhIwiRKCMmO3QNXgXNm5eHpdzbUFHIoAmGmiz5ThkCcQoo9WV1/jNQvDXfMUwfpa6Zb1CGNitlatFejgHCLVacXXfiLR+ZqdOeB2AUCuuYQxQ0PzueqOJWZ7q1acJPYDdu1B6weRLzA0N0tMyLmgyGbIQFAPV44/G8s6LeI+bHc/hhGHdvjBjnApcYWDdu3s3fbOIr5BVOX3lVPeDdNPGpTpYKX56W3yVksow6V4bH6MeSNgOZIJ2IxMRwdCGkgaNhi1/BX0q3WqPKh9zJqCeemAlYW4ABdo0=',
#     'AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg': '179643557%7CMCIDTS%7C19852%7CMCMID%7C29603892822686630342795742473154012872%7CMCAID%7CNONE%7CMCOPTOUT-1715153595s%7CNONE%7CMCAAMLH-1715751195%7C12%7CMCAAMB-1715751195%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19859%7CvVersion%7C5.5.0',
#     'RT': '"z=1&dm=www.yellowpages.com.au&si=60f2f6ab-b00f-4ddf-ab45-6c1ea53487e7&ss=lvxdvn6k&sl=9&tt=ij9&obo=4&rl=1&ld=1ufww&r=1cq8id2vp&ul=1ug64"',
#     's_ecid': 'MCMID%7C29603892822686630342795742473154012872',
#     'AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg': '1',
#     's_cc': 'true',
#     '_vwo_uuid_v2': 'DB99687685ECBB1AB6C00EEE87D884B22|6676e7e653d4442c937aca3b2592b838',
#     '_vis_opt_s': '1%7C',
#     '_vis_opt_test_cookie': '1',
#     '_vwo_uuid': 'DB99687685ECBB1AB6C00EEE87D884B22',
#     '_vwo_ds': '3%3Aa_0%2Ct_0%3A-1%241715146397%3A30.14756566%3A%3A%3A3_0%2C2_0%3A0',
#     '_vwo_sn': '0%3A9%3A%3A%3A1',
#     '_wingify_pc_uuid': 'bdce2bd8b1d54a88b264a22461f4172c',
#     'wingify_donot_track_actions': '0',
#     'bm_sv': '60B6224825835779ABA50369BEC2980B~YAAQdRwgF4cvjEiPAQAAjWfZVhelRYygP1sULBdlMplg67X1GejPPmh+vMjSiExv82BXabwVzyewbSocSD4t5FzXkcVbOesaDjaJ/H26LZD5mN5uBScjzo6Vd/qJ91rkMtyotCVC+ywuk32VuEgiNx9j9riSCrgaRlYch9Y2NDhEJtdXgjlP7/PzP8IMBXEI8YTAOBwZD52MgsGbyslF4UydTw6cDKAmZUBXPgMDynPlcepP8BToxOr7+e9d5uHVed7RwmHTb13Q~1',
#     's_sq': '%5B%5BB%5D%5D',
#     'yellow-guid': '1035f14e-bb83-4175-ba39-398eabe7e3c1',
#     'clue': '"lawyers solicitors"',
#     'locationClue': '"gold coast qld"',
#     '_vis_opt_exp_283_combi': '1',
#     '__gsas': 'ID=d8520f4ecbe34356:T=1715146833:RT=1715146833:S=ALNI_MZVQ_KBMC23MIAtz0rkuoGmpsqM5g',
#     '_vis_opt_exp_283_goal_5': '1',
#     '_vis_opt_exp_283_goal_1': '1',
#     'BVImplmain_site': '11347',
#     'BVBRANDID': '698974fa-f237-4ebe-bc12-21724d25182b',
#     'BVBRANDSID': 'b0f2f4f9-ccdf-4b41-b5a0-fceb545e5869',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.google.com/',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'ak_bmsc=EB9FF2783882A3E92AB4B33AD9C3AB0A~000000000000000000000000000000~YAAQbRwgF3XnmlCPAQAAjBCxVheEhFcGAZXwCCNVMh+xlEcHe0S6Y2tEiAOE/jdUSR+wUojREk646IUiRflKXdvPrNINIXrdC/cHGnzqC4wYuvrYBiC2JGizN2r4/W5Iisoo0lVkyg+CX9guVk57AQiBJ7BxLQWpy/4Yqmqtum8JKb/NWz4OgT3bQfEhIwiRKCMmO3QNXgXNm5eHpdzbUFHIoAmGmiz5ThkCcQoo9WV1/jNQvDXfMUwfpa6Zb1CGNitlatFejgHCLVacXXfiLR+ZqdOeB2AUCuuYQxQ0PzueqOJWZ7q1acJPYDdu1B6weRLzA0N0tMyLmgyGbIQFAPV44/G8s6LeI+bHc/hhGHdvjBjnApcYWDdu3s3fbOIr5BVOX3lVPeDdNPGpTpYKX56W3yVksow6V4bH6MeSNgOZIJ2IxMRwdCGkgaNhi1/BX0q3WqPKh9zJqCeemAlYW4ABdo0=; AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=179643557%7CMCIDTS%7C19852%7CMCMID%7C29603892822686630342795742473154012872%7CMCAID%7CNONE%7CMCOPTOUT-1715153595s%7CNONE%7CMCAAMLH-1715751195%7C12%7CMCAAMB-1715751195%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19859%7CvVersion%7C5.5.0; RT="z=1&dm=www.yellowpages.com.au&si=60f2f6ab-b00f-4ddf-ab45-6c1ea53487e7&ss=lvxdvn6k&sl=9&tt=ij9&obo=4&rl=1&ld=1ufww&r=1cq8id2vp&ul=1ug64"; s_ecid=MCMID%7C29603892822686630342795742473154012872; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; s_cc=true; _vwo_uuid_v2=DB99687685ECBB1AB6C00EEE87D884B22|6676e7e653d4442c937aca3b2592b838; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DB99687685ECBB1AB6C00EEE87D884B22; _vwo_ds=3%3Aa_0%2Ct_0%3A-1%241715146397%3A30.14756566%3A%3A%3A3_0%2C2_0%3A0; _vwo_sn=0%3A9%3A%3A%3A1; _wingify_pc_uuid=bdce2bd8b1d54a88b264a22461f4172c; wingify_donot_track_actions=0; bm_sv=60B6224825835779ABA50369BEC2980B~YAAQdRwgF4cvjEiPAQAAjWfZVhelRYygP1sULBdlMplg67X1GejPPmh+vMjSiExv82BXabwVzyewbSocSD4t5FzXkcVbOesaDjaJ/H26LZD5mN5uBScjzo6Vd/qJ91rkMtyotCVC+ywuk32VuEgiNx9j9riSCrgaRlYch9Y2NDhEJtdXgjlP7/PzP8IMBXEI8YTAOBwZD52MgsGbyslF4UydTw6cDKAmZUBXPgMDynPlcepP8BToxOr7+e9d5uHVed7RwmHTb13Q~1; s_sq=%5B%5BB%5D%5D; yellow-guid=1035f14e-bb83-4175-ba39-398eabe7e3c1; clue="lawyers solicitors"; locationClue="gold coast qld"; _vis_opt_exp_283_combi=1; __gsas=ID=d8520f4ecbe34356:T=1715146833:RT=1715146833:S=ALNI_MZVQ_KBMC23MIAtz0rkuoGmpsqM5g; _vis_opt_exp_283_goal_5=1; _vis_opt_exp_283_goal_1=1; BVImplmain_site=11347; BVBRANDID=698974fa-f237-4ebe-bc12-21724d25182b; BVBRANDSID=b0f2f4f9-ccdf-4b41-b5a0-fceb545e5869',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'cross-site',
#     'Sec-Fetch-User': '?1',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# # response = requests.get('https://www.yellowpages.com.au/', cookies=cookies, headers=headers)

# # import requests


# response = requests.get('https://www.yellowpages.com.au/', cookies=cookies, headers=headers)

# s.headers.update(headers)
# # s.cookies.update(cookies)
# # list_all = [ ]
# def main_page():
    
#     soup = BS (response.text,"html.parser")

#     for x in soup.find_all("div","icon-container"):
#         links = "https://www.yellowpages.com.au" + x.find("a").get("href")
#         # print(links)
#         list_page(links)

# def list_page(list_links):
#     r = s.get(list_links)
#     # print("main_______",r.url)
#     soup = BS (r.text,"html.parser")
    
#     for x in soup.find_all("div","Box__Div-sc-dws99b-0 fYIHHU"):
#         links = "https://www.yellowpages.com.au" + x.find("a").get("href")
#         # print(links)
#         detail_page(links)

# def detail_page(detail_links):
#     r = s.get(detail_links)
#     # print(r.url)
#     soup = BS (r.text,"html.parser")
    
#     try:
#         name = soup.find("a","listing-name").text
#     except:
#         name = "none"
#     try:
#         brand_logo = soup.find("img","brand-logo").get("src")
#     except:
#         brand_logo = "none"
#     try:
#         work = soup.find("p","listing-short-description").text
#     except:
#         work = "none"
#     try:
#         address = soup.find("div","listing-address mappable-address mappable-address-with-poi").text
#     except:
#         address = "none"
#     try:
#         phone_no = soup.find("div","desktop-display-value").text
#     except:
#         phone_no = "none"
#     try:
#         email = soup.find("a","contact contact-main contact-email").get("href")
#     except:
#         email = "none"
#     try:
#         website = soup.find("a","contact contact-main contact-url").get("href")
#     except:
#         website = "none"
#     try:
#         time = soup.find("div","opening-hours-today opening-hours-one-period").text.strip()
#     except:
#         time = "none"
#     try:
#         location = soup.find("a","get-directions").get("href")
#     except:
#         location = "none"
#     try:
#         image = []
#         for x in soup.find_all("img","rsTmb"):
#             image.append(x.get("src"))
#     except:
#         image = "none"
#     try:
#         about_us = soup.find("div","listing-descriptors about-us-section").text.strip()
#     except:
#         about_us = "none"
#     try:
#         social_media = []
#         for x in soup.find_all("span","img-text"):
#             social_media.append(x.find("a").get("href"))
#     except:
#         social_media = "none"
#     # print(social_media)
#     data.append({
#         "name" : name,
#         "brand_logo" : brand_logo,
#         "work" : work,
#         "address" : address,
#         "phone_no" : phone_no,
#         "email" :  email,
#         "website" : website,
#         "time" : time,
#         "location" : location,
#         "image" : image,
#         "about_us" : about_us,
#         "social_media" : social_media
#     })

#     print(data)
# #     # print(r.url)
 
  










# import requests 
# from bs4 import BeautifulSoup as BS
# url="https://www.yellowpages.com.au/"
# r=requests.get(url)
# soup=BS(r.text,"html.parser")
# for i in soup.find_all("div","icon-container"):
#     links="https://www.yellowpages.com.au/"+i.find("a").get("href")

# import requests

# cookies = {
#     'AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg': '179643557%7CMCIDTS%7C19859%7CMCMID%7C73433605071987196672777361658631663647%7CMCAID%7CNONE%7CMCOPTOUT-1715758413s%7CNONE%7CMCAAMLH-1716356013%7C12%7CMCAAMB-1716356013%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19864%7CvVersion%7C5.5.0',
#     'RT': '"z=1&dm=www.yellowpages.com.au&si=504a1d7b-d096-48e5-98a0-c977fc3b0475&ss=lw7dz06f&sl=0&tt=0"',
#     's_ecid': 'MCMID%7C73433605071987196672777361658631663647',
#     '_vwo_uuid_v2': 'DD21D120670C573D151A867286840E1D3|2f8ecb24e9fea0e6f8c3a1637431a3c3',
#     '_vis_opt_s': '3%7C',
#     '_vwo_uuid': 'DD21D120670C573D151A867286840E1D3',
#     '_vwo_ds': '3%3At_0%2Ca_0%3A-1%241715579488%3A68.28148336%3A%3A%3A3_0%2C2_0%3A0',
#     '_wingify_pc_uuid': 'ec6217b4937142aab909988f5d8fd9bf',
#     'wingify_donot_track_actions': '0',
#     '_vis_opt_exp_283_combi': '2',
#     '__gsas': 'ID=55494472982ae057:T=1715579649:RT=1715579649:S=ALNI_MacoVUhzjHMhPasUyUcspwgAhCmjg',
#     '_vis_opt_exp_283_goal_1': '1',
#     'BVBRANDID': '972823cb-a602-405b-a0d7-0c759e5e9425',
#     '__gads': 'ID=26a3250237fca51a:T=1715579684:RT=1715581835:S=ALNI_MaJ4rxHpInpjxXC1OqgetK2piuaRw',
#     '__gpi': 'UID=00000e1a2aab6ff8:T=1715579684:RT=1715581835:S=ALNI_MaVto3_M_7ijbJezNMMParPIrfwrg',
#     '__eoi': 'ID=53b854c70301e844:T=1715579684:RT=1715581835:S=AA-AfjZdT03ryCggMqG0ewIKrm7O',
#     'ak_bmsc': '041705E5C55ED6BB38AB84228B0131DD~000000000000000000000000000000~YAAQbRwgFy6g7lCPAQAASNu9eheWjvvtWaI2kk68xJV13GnELQ2gPRYvveUu1Y1zFZSrzhOQCFvcqtA5I5YfmbUsYtXkANaDBGDbYdrH/m+Uxf5CDMa6j9iPh+INWF18pJyq2atmqCBwwuSxpMheLN5fKxlSCJXalrDZVusLDVYeI0U96mtE5tBN18WDM9FAd/aWrMJ9ace2rxanqMDox7npFeudTHcUqGnCHlc/R+W5vzm3Sotq+tbVc6jUiN0lkJZ/VdAKOxIGpfKfkiaJuujzxEEVY8AGCQEeXoK9JMK7k9mYCkg53/ASEjnLZ3jSFoUSZzwYYJNIgLpqbHERJXbZwrBdMsNjN16RqIC5WIGnMPjV0D+1Dv8W7z2vEgTETgBadxdzEL7Xlw5DgHIJQU6WdDVjCkRKGQ55YifMUKH5N9cLOJBGfcJ+upOJYHrJlV3SE7ckr0zIYKPx7h8f49KCmow=',
#     'AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg': '1',
#     's_cc': 'true',
#     '_vis_opt_test_cookie': '1',
#     '_vwo_sn': '171726%3A1',
#     's_sq': 'telstrassyellowpagesprd%3D%2526c.%2526a.%2526activitymap.%2526page%253DSD%25253ADir%25253AYP%25253ASearch%25253Ayellow.com.au%2526link%253DLawyers%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DSD%25253ADir%25253AYP%25253ASearch%25253Ayellow.com.au%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.yellowpages.com.au%25252Ffind%25252Flawyers-solicitors%25252Fgold-coast-qld%2526ot%253DA',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.yellowpages.com.au/',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=179643557%7CMCIDTS%7C19859%7CMCMID%7C73433605071987196672777361658631663647%7CMCAID%7CNONE%7CMCOPTOUT-1715758413s%7CNONE%7CMCAAMLH-1716356013%7C12%7CMCAAMB-1716356013%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19864%7CvVersion%7C5.5.0; RT="z=1&dm=www.yellowpages.com.au&si=504a1d7b-d096-48e5-98a0-c977fc3b0475&ss=lw7dz06f&sl=0&tt=0"; s_ecid=MCMID%7C73433605071987196672777361658631663647; _vwo_uuid_v2=DD21D120670C573D151A867286840E1D3|2f8ecb24e9fea0e6f8c3a1637431a3c3; _vis_opt_s=3%7C; _vwo_uuid=DD21D120670C573D151A867286840E1D3; _vwo_ds=3%3At_0%2Ca_0%3A-1%241715579488%3A68.28148336%3A%3A%3A3_0%2C2_0%3A0; _wingify_pc_uuid=ec6217b4937142aab909988f5d8fd9bf; wingify_donot_track_actions=0; _vis_opt_exp_283_combi=2; __gsas=ID=55494472982ae057:T=1715579649:RT=1715579649:S=ALNI_MacoVUhzjHMhPasUyUcspwgAhCmjg; _vis_opt_exp_283_goal_1=1; BVBRANDID=972823cb-a602-405b-a0d7-0c759e5e9425; __gads=ID=26a3250237fca51a:T=1715579684:RT=1715581835:S=ALNI_MaJ4rxHpInpjxXC1OqgetK2piuaRw; __gpi=UID=00000e1a2aab6ff8:T=1715579684:RT=1715581835:S=ALNI_MaVto3_M_7ijbJezNMMParPIrfwrg; __eoi=ID=53b854c70301e844:T=1715579684:RT=1715581835:S=AA-AfjZdT03ryCggMqG0ewIKrm7O; ak_bmsc=041705E5C55ED6BB38AB84228B0131DD~000000000000000000000000000000~YAAQbRwgFy6g7lCPAQAASNu9eheWjvvtWaI2kk68xJV13GnELQ2gPRYvveUu1Y1zFZSrzhOQCFvcqtA5I5YfmbUsYtXkANaDBGDbYdrH/m+Uxf5CDMa6j9iPh+INWF18pJyq2atmqCBwwuSxpMheLN5fKxlSCJXalrDZVusLDVYeI0U96mtE5tBN18WDM9FAd/aWrMJ9ace2rxanqMDox7npFeudTHcUqGnCHlc/R+W5vzm3Sotq+tbVc6jUiN0lkJZ/VdAKOxIGpfKfkiaJuujzxEEVY8AGCQEeXoK9JMK7k9mYCkg53/ASEjnLZ3jSFoUSZzwYYJNIgLpqbHERJXbZwrBdMsNjN16RqIC5WIGnMPjV0D+1Dv8W7z2vEgTETgBadxdzEL7Xlw5DgHIJQU6WdDVjCkRKGQ55YifMUKH5N9cLOJBGfcJ+upOJYHrJlV3SE7ckr0zIYKPx7h8f49KCmow=; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; s_cc=true; _vis_opt_test_cookie=1; _vwo_sn=171726%3A1; s_sq=telstrassyellowpagesprd%3D%2526c.%2526a.%2526activitymap.%2526page%253DSD%25253ADir%25253AYP%25253ASearch%25253Ayellow.com.au%2526link%253DLawyers%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DSD%25253ADir%25253AYP%25253ASearch%25253Ayellow.com.au%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.yellowpages.com.au%25252Ffind%25252Flawyers-solicitors%25252Fgold-coast-qld%2526ot%253DA',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# response = requests.get(
#     'https://www.yellowpages.com.au/find/lawyers-solicitors/gold-coast-qld',
#     cookies=cookies,
#     headers=headers,
# )
# r_1=requests.get(links)
# soup_1=BS(response.text,"html.parser")


# for j in soup_1("div","Box__Div-sc-dws99b-0 fYIHHU"):
#     links_1="https://www.yellowpages.com.au"+j.find("a").get("href")

#     import requests

# cookies = {
#     'AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg': '179643557%7CMCIDTS%7C19859%7CMCMID%7C73433605071987196672777361658631663647%7CMCAID%7CNONE%7CMCOPTOUT-1715758413s%7CNONE%7CMCAAMLH-1716356013%7C12%7CMCAAMB-1716356013%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19864%7CvVersion%7C5.5.0',
#     'RT': '"z=1&dm=www.yellowpages.com.au&si=504a1d7b-d096-48e5-98a0-c977fc3b0475&ss=lw7gm682&sl=4&tt=aib&obo=2&rl=1&nu=1cq8id2vp&cl=wnpd&ld=wnjl&r=2w3b93f1&ul=wnrd"',
#     's_ecid': 'MCMID%7C73433605071987196672777361658631663647',
#     '_vwo_uuid_v2': 'DD21D120670C573D151A867286840E1D3|2f8ecb24e9fea0e6f8c3a1637431a3c3',
#     '_vis_opt_s': '3%7C',
#     '_vwo_uuid': 'DD21D120670C573D151A867286840E1D3',
#     '_vwo_ds': '3%3At_0%2Ca_0%3A-1%241715579488%3A68.28148336%3A%3A%3A3_0%2C2_0%3A0',
#     '_wingify_pc_uuid': 'ec6217b4937142aab909988f5d8fd9bf',
#     'wingify_donot_track_actions': '0',
#     '_vis_opt_exp_283_combi': '2',
#     '__gsas': 'ID=55494472982ae057:T=1715579649:RT=1715579649:S=ALNI_MacoVUhzjHMhPasUyUcspwgAhCmjg',
#     '_vis_opt_exp_283_goal_1': '1',
#     'BVBRANDID': '972823cb-a602-405b-a0d7-0c759e5e9425',
#     '__gads': 'ID=26a3250237fca51a:T=1715579684:RT=1715753510:S=ALNI_MaJ4rxHpInpjxXC1OqgetK2piuaRw',
#     '__gpi': 'UID=00000e1a2aab6ff8:T=1715579684:RT=1715753510:S=ALNI_MaVto3_M_7ijbJezNMMParPIrfwrg',
#     '__eoi': 'ID=53b854c70301e844:T=1715579684:RT=1715753510:S=AA-AfjZdT03ryCggMqG0ewIKrm7O',
#     'ak_bmsc': '041705E5C55ED6BB38AB84228B0131DD~000000000000000000000000000000~YAAQbRwgFy6g7lCPAQAASNu9eheWjvvtWaI2kk68xJV13GnELQ2gPRYvveUu1Y1zFZSrzhOQCFvcqtA5I5YfmbUsYtXkANaDBGDbYdrH/m+Uxf5CDMa6j9iPh+INWF18pJyq2atmqCBwwuSxpMheLN5fKxlSCJXalrDZVusLDVYeI0U96mtE5tBN18WDM9FAd/aWrMJ9ace2rxanqMDox7npFeudTHcUqGnCHlc/R+W5vzm3Sotq+tbVc6jUiN0lkJZ/VdAKOxIGpfKfkiaJuujzxEEVY8AGCQEeXoK9JMK7k9mYCkg53/ASEjnLZ3jSFoUSZzwYYJNIgLpqbHERJXbZwrBdMsNjN16RqIC5WIGnMPjV0D+1Dv8W7z2vEgTETgBadxdzEL7Xlw5DgHIJQU6WdDVjCkRKGQ55YifMUKH5N9cLOJBGfcJ+upOJYHrJlV3SE7ckr0zIYKPx7h8f49KCmow=',
#     'AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg': '1',
#     's_cc': 'true',
#     '_vis_opt_test_cookie': '1',
#     '_vwo_sn': '171726%3A15',
#     's_sq': 'telstrassyellowpagesprd%3D%2526c.%2526a.%2526activitymap.%2526page%253DSD%25253ADir%25253AYP%25253ASearch%25253AType%25253ABusiness%252520Listings%2526link%253DDwyer%252520Law%252520Group%2526region%253Droot%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DSD%25253ADir%25253AYP%25253ASearch%25253AType%25253ABusiness%252520Listings%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.yellowpages.com.au%25252Fqld%25252Fsurfers-paradise%25252Fdwyer-law-group-14973750-listing.html%2526ot%253DA',
#     'yellow-guid': '2c48c286-3003-41e9-9288-dde7dd668a8d',
#     'clue': '"lawyers solicitors"',
#     'locationClue': '"gold coast qld"',
#     'bm_sv': '16CF0C8D802CD614E5C39569326AD047~YAAQbRwgF9Oz71CPAQAA/HwOexfF4bgUEJHjAiX9THkx9C16mVSGh2P6lHr92avun9h89N89egoI6PLZ0l2jAFkiVsAlywNSHgakby3WQZiD6k8LvIooGfyar+6uWJHkUbk/GvIgVvPueP1J9aIw4IttVutlSAsX6HIF0n5f73s6GwLZANccDht6/7POlW/093Lj+Nm2F0b3lxux4+rs6egbs5WlHVUd4wYfD54RJYqh8qJacZ/tQDIrL840TKxiuxRpOMQr7bZs~1',
#     'BVImplmain_site': '11347',
#     '_vis_opt_exp_283_goal_5': '1',
#     'BVBRANDSID': '63ee07e9-2d25-4c33-adde-00a39116923a',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.yellowpages.com.au/find/lawyers-solicitors/gold-coast-qld',
#     # 'Cookie': 'AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=179643557%7CMCIDTS%7C19859%7CMCMID%7C73433605071987196672777361658631663647%7CMCAID%7CNONE%7CMCOPTOUT-1715758413s%7CNONE%7CMCAAMLH-1716356013%7C12%7CMCAAMB-1716356013%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19864%7CvVersion%7C5.5.0; RT="z=1&dm=www.yellowpages.com.au&si=504a1d7b-d096-48e5-98a0-c977fc3b0475&ss=lw7gm682&sl=4&tt=aib&obo=2&rl=1&nu=1cq8id2vp&cl=wnpd&ld=wnjl&r=2w3b93f1&ul=wnrd"; s_ecid=MCMID%7C73433605071987196672777361658631663647; _vwo_uuid_v2=DD21D120670C573D151A867286840E1D3|2f8ecb24e9fea0e6f8c3a1637431a3c3; _vis_opt_s=3%7C; _vwo_uuid=DD21D120670C573D151A867286840E1D3; _vwo_ds=3%3At_0%2Ca_0%3A-1%241715579488%3A68.28148336%3A%3A%3A3_0%2C2_0%3A0; _wingify_pc_uuid=ec6217b4937142aab909988f5d8fd9bf; wingify_donot_track_actions=0; _vis_opt_exp_283_combi=2; __gsas=ID=55494472982ae057:T=1715579649:RT=1715579649:S=ALNI_MacoVUhzjHMhPasUyUcspwgAhCmjg; _vis_opt_exp_283_goal_1=1; BVBRANDID=972823cb-a602-405b-a0d7-0c759e5e9425; __gads=ID=26a3250237fca51a:T=1715579684:RT=1715753510:S=ALNI_MaJ4rxHpInpjxXC1OqgetK2piuaRw; __gpi=UID=00000e1a2aab6ff8:T=1715579684:RT=1715753510:S=ALNI_MaVto3_M_7ijbJezNMMParPIrfwrg; __eoi=ID=53b854c70301e844:T=1715579684:RT=1715753510:S=AA-AfjZdT03ryCggMqG0ewIKrm7O; ak_bmsc=041705E5C55ED6BB38AB84228B0131DD~000000000000000000000000000000~YAAQbRwgFy6g7lCPAQAASNu9eheWjvvtWaI2kk68xJV13GnELQ2gPRYvveUu1Y1zFZSrzhOQCFvcqtA5I5YfmbUsYtXkANaDBGDbYdrH/m+Uxf5CDMa6j9iPh+INWF18pJyq2atmqCBwwuSxpMheLN5fKxlSCJXalrDZVusLDVYeI0U96mtE5tBN18WDM9FAd/aWrMJ9ace2rxanqMDox7npFeudTHcUqGnCHlc/R+W5vzm3Sotq+tbVc6jUiN0lkJZ/VdAKOxIGpfKfkiaJuujzxEEVY8AGCQEeXoK9JMK7k9mYCkg53/ASEjnLZ3jSFoUSZzwYYJNIgLpqbHERJXbZwrBdMsNjN16RqIC5WIGnMPjV0D+1Dv8W7z2vEgTETgBadxdzEL7Xlw5DgHIJQU6WdDVjCkRKGQ55YifMUKH5N9cLOJBGfcJ+upOJYHrJlV3SE7ckr0zIYKPx7h8f49KCmow=; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; s_cc=true; _vis_opt_test_cookie=1; _vwo_sn=171726%3A15; s_sq=telstrassyellowpagesprd%3D%2526c.%2526a.%2526activitymap.%2526page%253DSD%25253ADir%25253AYP%25253ASearch%25253AType%25253ABusiness%252520Listings%2526link%253DDwyer%252520Law%252520Group%2526region%253Droot%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DSD%25253ADir%25253AYP%25253ASearch%25253AType%25253ABusiness%252520Listings%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.yellowpages.com.au%25252Fqld%25252Fsurfers-paradise%25252Fdwyer-law-group-14973750-listing.html%2526ot%253DA; yellow-guid=2c48c286-3003-41e9-9288-dde7dd668a8d; clue="lawyers solicitors"; locationClue="gold coast qld"; bm_sv=16CF0C8D802CD614E5C39569326AD047~YAAQbRwgF9Oz71CPAQAA/HwOexfF4bgUEJHjAiX9THkx9C16mVSGh2P6lHr92avun9h89N89egoI6PLZ0l2jAFkiVsAlywNSHgakby3WQZiD6k8LvIooGfyar+6uWJHkUbk/GvIgVvPueP1J9aIw4IttVutlSAsX6HIF0n5f73s6GwLZANccDht6/7POlW/093Lj+Nm2F0b3lxux4+rs6egbs5WlHVUd4wYfD54RJYqh8qJacZ/tQDIrL840TKxiuxRpOMQr7bZs~1; BVImplmain_site=11347; _vis_opt_exp_283_goal_5=1; BVBRANDSID=63ee07e9-2d25-4c33-adde-00a39116923a',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# response = requests.get(
#     'https://www.yellowpages.com.au/qld/surfers-paradise/dwyer-law-group-14973750-listing.html',
#     cookies=cookies,
#     headers=headers,
# )
# r_2=requests.get(url)
# soup_2=BS(response.text,"html.parser")

# try:
#     name = soup_2.find_all("a","listing-name")
# except:
#     name = None
# print(name)


import requests
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.yellowpages.com.au/',
    'Connection': 'keep-alive',
    # 'Cookie': 'AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=179643557%7CMCIDTS%7C19862%7CMCMID%7C73433605071987196672777361658631663647%7CMCAID%7CNONE%7CMCOPTOUT-1716024586s%7CNONE%7CMCAAMLH-1716622186%7C12%7CMCAAMB-1716622186%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19864%7CvVersion%7C5.5.0; RT="z=1&dm=www.yellowpages.com.au&si=504a1d7b-d096-48e5-98a0-c977fc3b0475&ss=lwbo27mz&sl=8&tt=x4r&obo=4&rl=1&ld=4e9yn&r=2w3b93f1&ul=4e9yw"; s_ecid=MCMID%7C73433605071987196672777361658631663647; _vwo_uuid_v2=DD21D120670C573D151A867286840E1D3|2f8ecb24e9fea0e6f8c3a1637431a3c3; _vis_opt_s=3%7C; _vwo_uuid=DD21D120670C573D151A867286840E1D3; _vwo_ds=3%3At_0%2Ca_0%3A-1%241715579488%3A68.28148336%3A%3A%3A3_0%2C2_0%3A0; _wingify_pc_uuid=ec6217b4937142aab909988f5d8fd9bf; wingify_donot_track_actions=0; _vis_opt_exp_283_combi=2; __gsas=ID=55494472982ae057:T=1715579649:RT=1715579649:S=ALNI_MacoVUhzjHMhPasUyUcspwgAhCmjg; _vis_opt_exp_283_goal_1=1; BVBRANDID=972823cb-a602-405b-a0d7-0c759e5e9425; __gads=ID=26a3250237fca51a:T=1715579684:RT=1715837043:S=ALNI_MaJ4rxHpInpjxXC1OqgetK2piuaRw; __gpi=UID=00000e1a2aab6ff8:T=1715579684:RT=1715837043:S=ALNI_MaVto3_M_7ijbJezNMMParPIrfwrg; __eoi=ID=53b854c70301e844:T=1715579684:RT=1715837043:S=AA-AfjZdT03ryCggMqG0ewIKrm7O; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; s_cc=true; _vis_opt_test_cookie=1; s_sq=%5B%5BB%5D%5D; yellow-guid=2c48c286-3003-41e9-9288-dde7dd668a8d; BVImplmain_site=11347; _vis_opt_exp_283_goal_5=1; ypolAnnouncementViewed=true; _vwo_sn=434881%3A4; clue="lawyers solicitors"; locationClue="gold coast qld"; ak_bmsc=B9836D9B918C02A3B7C943D2C2A16DDF~000000000000000000000000000000~YAAQbRwgF7TpFlGPAQAA6HabihdRZmmedf3B6EU1PlCWGs7M/P0Dwydf/De8iEzGqmsFm4KcVHs6ERXKPDzjpAA6seGk3KdRmPGM+z+xclY6xfY4Ne5SZiIZtzh1l4DLD9ULscEKXFgl32jnZamHiwTXw94K4hMpUeN92TQljO8GewWJpXrL4MQftYx2WdUvpnF1eeLSVoVSfENQfetQSHNjofDh65kdifYg3aGKwKukrshvjNAmkmqKuVTLtiLlv9t/5Rf2wKnToPE7NXDfcCr9J7o7QqxQU8xyHECGV9NyotSsvwDBI2FBCCWiS44im3OAKV5xrJ3cho/OQ2JT0rHTJ4zdNDYHrXXrrdJaAIAFcdULKLpBFE8XVrsNasqmmN3UqkZZfsa/ZRos735K8b/W4i9CJGcApRdCc3ADHfr6Mm80c21kZLxZmAnGpL6B3ZJyGsrH1dtTUzeO/+xNBOXF1UM=; bm_sv=0833FAECAAC0B842C3491D02EDE4502A~YAAQbRwgF+vpFlGPAQAAC4ibihfpNBR9sc1kRobwpVituywXmZGrJLSXd/e7eSdskga/pZ44ce0mh2LbVpDDQVBcID4kS7mjTwglMM8syq3ndHSmATlrlUGeFNhMl9J4qY/lOJ9NENPT0KxDic3AV5MQRYDXI/uFQi8f3PGUmhG1iP9R9i/eGaA5o5FNoCUgYKSWmqR541suwWuUWR9Q5VLUMKYqTLUi00U3ItrNWJG61v6vDuoD57S+/S408rV2wpTSoELWgYo=~1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}


url="https://www.yellowpages.com.au"
r=requests.get(url,headers=headers)
soup=BS(r.text,"html.parser")
for i in soup.find("div","homepage-quicklinks-container").find_all("div","icon-container"):
    links="https://www.yellowpages.com.au"+i.find("a").get("href")
    # print(links)
    r1=requests.get(links,headers=headers)
    soup1=BS(r1.text,"html.parser")
    for j in soup1.find_all("div","Box__Div-sc-dws99b-0 fYIHHU"):
        linkss=("https://www.yellowpages.com.au"+j.find("a").get("href"))
        r2=requests.get(linkss,headers=headers)
        soup2=BS(r2.text,"html.parser")
        try:
            title=soup2.find("a","listing-name").text.strip()
        except:
            title="not available"
        try:
            address=soup2.find("div","listing-address mappable-address mappable-address-with-poi").text.strip()
        except:
            address="address not available"
        try:
            brand_logo=soup2.find("img","brand-logo").get("src")
        except:
            brand_logo="not availab le brand-logo"
        print(brand_logo)

        
