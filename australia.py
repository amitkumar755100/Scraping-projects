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
# list_all = [ ]
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
#     print(r.url)

# main_page()

# df = pd.DataFrame(data)
# df.to_excel("yellowpages_aus.xlsx")
