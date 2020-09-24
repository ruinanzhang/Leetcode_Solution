import requests
from pprint import pprint  

history = {}
# Get author about data 
base_url = "https://jsonmock.hackerrank.com/api/article_users?username="
author_name = "saintamh"
auth_info_url = base_url+ author_name+"&page=1"
r_info = requests.get(auth_info_url)
r_info_json = r_info.json()
pprint(r_info_json )
info_data = r_info_json['data']
if info_data[0]['about']:
    about = info_data[0]['about']
else: 
    about = None
history['about'] = about 
# print(r_info_json)
# print(about)
# print(history)
base_url_2 = "https://jsonmock.hackerrank.com/api/articles?author="
auth_title_url = base_url_2 + author_name +"&page=1"
r_title = requests.get(auth_title_url )
r_title_json = r_title.json()
total_title_page = r_title_json['total_pages']
auth_title =[]
for p_index in  range(1,total_title_page+1):
    curr_url = base_url_2 + author_name + "&page=" + str(p_index)
    res = requests.get(curr_url)
    res_json = res.json()
    data = res_json['data']
    for each_data in data:
        if each_data['title']:
            auth_title.append(each_data['title'])
        elif not each_data['title'] and each_data['story_title']:
            auth_title.append(each_data['story_title'])
        elif not each_data['title'] and not each_data['story_title']:
            continue 
history["title"]= auth_title
print(history)


# print(r_title_json)



