# import requests
# import re


# cookies = {
#     'T': 'clx4xa9ai16mc1eeqyc6073sc-BR1717779033738',
#     'SN': 'VI39D3FBE634474B26B1B45AF076D399E5.TOKD190FE3EB8534546B5C7BC556A3DF318.1717992799.LO',
#     'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTk1MDcwMzMsImlhdCI6MTcxNzc3OTAzMywiaXNzIjoia2V2bGFyIiwianRpIjoiODdmM2RjNzItYWNlNi00MWY0LThiMTAtNzczNGE3YTVkM2IyIiwidHlwZSI6IkFUIiwiZElkIjoiY2x4NHhhOWFpMTZtYzFlZXF5YzYwNzNzYy1CUjE3MTc3NzkwMzM3MzgiLCJrZXZJZCI6IlZJMzlEM0ZCRTYzNDQ3NEIyNkIxQjQ1QUYwNzZEMzk5RTUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.kH8ex7Ekft-nCC_OgXBdeGzENUXqsOGezwvdWpb0VHc',
#     'K-ACTION': 'null',
#     'ud': '3.-hCuLDZfVJf9kwEcWhK4ak81dHd_VXurwOTlZ2O8JI48Ji-Lv_59dSq0VGCEESQL22yPn6dN90-RyfoPliG_nD7yXbi0O9bMpq_Afbr3h1jEhWaUKV1lWF0JubqC1k8e47Y4lGE4oowuX3dkUsJZeA',
#     'vh': '416',
#     'vw': '1536',
#     'dpr': '1.25',
#     'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19884%7CMCMID%7C44006127208302256003032398615234181034%7CMCAAMLH-1718383832%7C12%7CMCAAMB-1718511816%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1717914216s%7CNONE%7CMCAID%7CNONE',
#     '_pxvid': '1029dd35-24ee-11ef-986c-e250734ec9f6',
#     'vd': 'VI39D3FBE634474B26B1B45AF076D399E5-1717779056568-4.1717992799.1717992799.154671030',
#     'rt': 'null',
#     'S': 'd1t16Fz8/P3YWMTs2PzU/Pz8/P10xilcD5TcV8+msG0mnoDIkhILPBghBWLHc2IJSzzdVOIHbBG2LtylOrUH66W7Icw==',
#     '_px3': 'e263c0bfbb34d7fb0d20ade8f53ef9e13b94812cf92d9d3cca2b9c620840d409:YAx0yMm9jZQKstFIIfJWXZcP+5JSPe/7BUZXpBrrrqmBnNtGtGa9o0oDBU3OqTSkQm1ZO6Qswj2YfTU+sZss1A==:1000:Xl6CIbEq7075N0/piz+edKXZRURZj0LxoCo5f70vQtWzbG9jZauLDhAFz4M8It079WS2Td6yWOjQ1oPKyb6DilwqAhVKckykg/6VPYnsbg4TbPtcM66/zwoJLDUyow6ck5x2ovwoq6iO/YMt7s9Thc6gbE5LuS8haFlB9qqxD+33EczU+rzmETiSiqOWhoCGq84Qu2txFXybbL0PADUkVofduQEaY86MSCQ/vSd5ZrM=',
#     'pxcts': 'c68e1766-26df-11ef-8e8f-2f27fb793a23',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'T=clx4xa9ai16mc1eeqyc6073sc-BR1717779033738; SN=VI39D3FBE634474B26B1B45AF076D399E5.TOKD190FE3EB8534546B5C7BC556A3DF318.1717992799.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTk1MDcwMzMsImlhdCI6MTcxNzc3OTAzMywiaXNzIjoia2V2bGFyIiwianRpIjoiODdmM2RjNzItYWNlNi00MWY0LThiMTAtNzczNGE3YTVkM2IyIiwidHlwZSI6IkFUIiwiZElkIjoiY2x4NHhhOWFpMTZtYzFlZXF5YzYwNzNzYy1CUjE3MTc3NzkwMzM3MzgiLCJrZXZJZCI6IlZJMzlEM0ZCRTYzNDQ3NEIyNkIxQjQ1QUYwNzZEMzk5RTUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.kH8ex7Ekft-nCC_OgXBdeGzENUXqsOGezwvdWpb0VHc; K-ACTION=null; ud=3.-hCuLDZfVJf9kwEcWhK4ak81dHd_VXurwOTlZ2O8JI48Ji-Lv_59dSq0VGCEESQL22yPn6dN90-RyfoPliG_nD7yXbi0O9bMpq_Afbr3h1jEhWaUKV1lWF0JubqC1k8e47Y4lGE4oowuX3dkUsJZeA; vh=416; vw=1536; dpr=1.25; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19884%7CMCMID%7C44006127208302256003032398615234181034%7CMCAAMLH-1718383832%7C12%7CMCAAMB-1718511816%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1717914216s%7CNONE%7CMCAID%7CNONE; _pxvid=1029dd35-24ee-11ef-986c-e250734ec9f6; vd=VI39D3FBE634474B26B1B45AF076D399E5-1717779056568-4.1717992799.1717992799.154671030; rt=null; S=d1t16Fz8/P3YWMTs2PzU/Pz8/P10xilcD5TcV8+msG0mnoDIkhILPBghBWLHc2IJSzzdVOIHbBG2LtylOrUH66W7Icw==; _px3=e263c0bfbb34d7fb0d20ade8f53ef9e13b94812cf92d9d3cca2b9c620840d409:YAx0yMm9jZQKstFIIfJWXZcP+5JSPe/7BUZXpBrrrqmBnNtGtGa9o0oDBU3OqTSkQm1ZO6Qswj2YfTU+sZss1A==:1000:Xl6CIbEq7075N0/piz+edKXZRURZj0LxoCo5f70vQtWzbG9jZauLDhAFz4M8It079WS2Td6yWOjQ1oPKyb6DilwqAhVKckykg/6VPYnsbg4TbPtcM66/zwoJLDUyow6ck5x2ovwoq6iO/YMt7s9Thc6gbE5LuS8haFlB9qqxD+33EczU+rzmETiSiqOWhoCGq84Qu2txFXybbL0PADUkVofduQEaY86MSCQ/vSd5ZrM=; pxcts=c68e1766-26df-11ef-8e8f-2f27fb793a23',
#     'Priority': 'u=1',
# }
# def detail_pge():
#     response = requests.get(
#     'https://www.flipkart.com/kotty-regular-women-black-jeans/p/itmbd2194b7512df',
#     cookies=cookies,
#     headers=headers,
# )
#     response.text
#     list=[]
#     # print(response.text)

#     try:
#         name=re.search('"VU-ZEz">(.*?)</span>', response.text).group(1)
#     except:
#         name="name is not available"
#     try:
#         image=[]

#         data=re.findall('"DByuf4 IZexXJ jLEJ7H"(.*?)</div>',response.text)
#         for i in data:
#             image.append(re.search('src="(.*)' ,i).group(1))
#     except:
#         image="not available image"
#     try:
#         price=re.search('"Nx9bqj CxhGGd">(.*?)</div>',response.text).group(1)
#     except:
#         price="price is not available"
#     try:
#         rating=re.search("Wphh3N(.*?)</div>",response.text).group(1).strip().replace('"><span>','').split('and')[0]
#         # rating=re.search("Wphh3N(.*?)</", response.text).group(1).strip().replace('"><span>','').split('and')[0]
#     except:
#         rating="rating is not available"
#     try:
#         review=re.search("Wphh3N(.*?)</", response.text).group(1).strip().replace('"><span>','').split('and')[1]
       
#     except:
#         review="review is not available"
#     try:
#         comments=[]
#         for y in re.findall('"_8-rIO3 iIbIvC">(.*?)/n', response.text):
#             comments.append(re.findall('"_11pzQk">(.*?)</div>', y)).replace
#     except:
#         comment="comment is not available"
    
#     list.append({
#         "name":name,
#         "price":price,
#         "rating":rating,
#         "review":review,
#         "image":image,
#         "comments":comments
#     })
#     print(list)


    

# detail_pge()
# name=re.search('"VU-ZEz">(.*?)</span>', response.text).group(1)
# print(name)




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
    
