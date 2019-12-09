import json
import sys

import requests
import time

millis = int(round(time.time() * 1000))
print(millis)
url = 'https://sso.toutiao.com/account_login/v2/'
head = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'origin': 'https://sso.toutiao.com',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://sso.toutiao.com/login/?service=https://mp.toutiao.com/sso_confirm/?redirect_url=JTJG',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cookie': '_ga=GA1.2.944108445.1563354738; __tea_sdk__ssid=6d77ade1-fa90-4de9-842f-35038a912dac; tt_webid=6716304404033226251; __tea_sdk__user_unique_id=6716304404033226251; UM_distinctid=16c235074cd80b-0f435e6cd7e287-37637c02-1fa400-16c235074cea31; uuid="w:4386723d881049049c49e6f08decdf7a"; __utma=24953151.944108445.1563354738.1566720749.1567050096.2; __utmz=24953151.1567050096.2.2.utmcsr=mp.toutiao.com|utmccn=(referral)|utmcmd=referral|utmcct=/profile_v3/column/chapter-edit-richtext; sso_auth_status=adf5432b0670968bf1d247eaab427863%2C91e7fb1a944c285312c62c1de2499b99; _mp_auth_key=adf5432b0670968bf1d247eaab427863; install_id=0; ccid=c258aada0463ecb920b15ab856836466; _gid=GA1.2.1082824914.1575612326; msh=jnFuDzrFUQxRYO5s07XxqeOMTLs; ttcid=5a6ce5239cca4675a6fc2c08f1e1196239; passport_auth_status=754ae0289f52d689662941c03c924cac%2C032fa970a916a2238a4b541da18f8818; s_v_web_id=1675248e5f935235a8ef272cccd79575; toutiao_sso_user=0de10d7f2783e8ad3af70149237d0fab; sid_guard=8fdc716c5594e4709c060f1011595cd0%7C1575617028%7C5184000%7CTue%2C+04-Feb-2020+07%3A23%3A48+GMT; uid_tt=eb8fa2e2e1d828db5c171047cdd878c0; sid_tt=8fdc716c5594e4709c060f1011595cd0; sessionid=8fdc716c5594e4709c060f1011595cd0; sso_uid_tt=9949c451ce0612b3f9b37a6935ce1313',
}

params = {
    'aid': 24,
    'service': "https://mp.toutiao.com/sso_confirm/?redirect_url=JTJG",
    'account_sdk_source': 'sso',
    'mix_mode': 1,
    'fp': '1675248e5f935235a8ef272cccd79575',
    'password': '7d6c602b34303c3230362b',
    'account': '34303330343d353d3c3430',
    'web_timestamp': str(millis)
}
r = requests.post(url, headers=head, params=params)
jsonData = json.loads(r.text)
print(jsonData)
