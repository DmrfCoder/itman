import json
import sys

import requests
import time
millis = int(round(time.time() * 1000))
print(millis)
url = 'https://mp.toutiao.com/mp/agw/article/new'
head = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://mp.toutiao.com/profile_v3/graphic/publish',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cookie': '_ga=GA1.2.944108445.1563354738; __tea_sdk__ssid=6d77ade1-fa90-4de9-842f-35038a912dac; tt_webid=6716304404033226251; __tea_sdk__user_unique_id=6716304404033226251; UM_distinctid=16c235074cd80b-0f435e6cd7e287-37637c02-1fa400-16c235074cea31; connect.sid=s%3AZHYPdrSDFOkxoczoJFZqw_EmTaXLnES7.AlELf1YRq%2BDMhCXcVirRJPgmk1%2B7OMw0wN0ANj5NOTg; _ba=BA0.2-20190805-5110e-Bqd7uX6imGSWdpycZtnb; uuid="w:4386723d881049049c49e6f08decdf7a"; __utma=24953151.944108445.1563354738.1566720749.1567050096.2; __utmz=24953151.1567050096.2.2.utmcsr=mp.toutiao.com|utmccn=(referral)|utmcmd=referral|utmcct=/profile_v3/column/chapter-edit-richtext; SLARDAR_WEB_ID=2300289d-d3ff-47f3-9894-72de3760e74a; sso_auth_status=adf5432b0670968bf1d247eaab427863%2C91e7fb1a944c285312c62c1de2499b99; _mp_auth_key=adf5432b0670968bf1d247eaab427863; _mp_auth_key=adf5432b0670968bf1d247eaab427863; install_id=0; ccid=c258aada0463ecb920b15ab856836466; s_v_web_id=ceb5f62aa3b952b2890a66b251a91b26; _gid=GA1.2.1082824914.1575612326; msh=jnFuDzrFUQxRYO5s07XxqeOMTLs; sso_uid_tt=d4f7eaf5d7d77307cb8c676f62d78dca; toutiao_sso_user=aafa894460025dbf568cf298c9e6013c; passport_auth_status=032fa970a916a2238a4b541da18f8818%2C2ac9092f8bf9510eae3d264a1b704348; sid_guard=98864f4322d0ab2bb7a72460dd5b24a9%7C1575613238%7C5184000%7CTue%2C+04-Feb-2020+06%3A20%3A38+GMT; uid_tt=07adaacc03964c42644a97e58003d131; sid_tt=98864f4322d0ab2bb7a72460dd5b24a9; sessionid=98864f4322d0ab2bb7a72460dd5b24a9',
}

params = {
    'article_type': 0,
    'format': "json",
    'compat': 1,
    'column_no': '',
}
r = requests.get(url, headers=head, params=params)
jsonData = json.loads(r.text)
data=jsonData['data']
media_id=data['media_id']
#
# print(jsonData)