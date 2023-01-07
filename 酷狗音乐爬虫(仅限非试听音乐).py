import pprint

import requests
import re
headers1={
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'cookie':'kg_mid=36cafbb62a65fbbc7ab3480162172741; kg_dfid=4XTDlO0Tjyl827K26B2JOWFJ; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=36cafbb62a65fbbc7ab3480162172741',
    'referer':'https://www.kugou.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
}
headers2={
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'cookie':'kg_mid=36cafbb62a65fbbc7ab3480162172741; kg_dfid=4XTDlO0Tjyl827K26B2JOWFJ; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
url=input("请输入音乐网址：")
print("正在获取歌曲信息.....")
response_1=requests.get(url=url,headers=headers1)
hash1=re.findall('"hash":"(.*?)"',response_1.text)[0]
album_id=re.findall(',"album_id":(.*?),',response_1.text)[0]
song_url=f"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hash1}&dfid=4XTDlO0Tjyl827K26B2JOWFJ&appid=1014&mid=36cafbb62a65fbbc7ab3480162172741&platid=4&album_id={album_id}&_=1649986632571"
response=requests.get(headers=headers2,url=song_url).json()
pprint.pprint(response)
audio_url=response['data']['play_url']
songname=response['data']['song_name']
songname_1=songname.replace(' ','_')
print("正在下载歌曲....")
audio_content=requests.get(headers=headers1,url=audio_url).content
with open(songname_1+'.mp3',mode='wb')as f:
    f.write(audio_content)

