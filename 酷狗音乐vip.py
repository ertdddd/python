import os
import urllib3
import requests
import re
headers={
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'dnt':'1',
'origin':'https://www.kugou.com',
'referer':'https://www.kugou.com/',
'sec-ch-ua':'" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'sec-gpc':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}
url=input("请输入音乐网址：")
url_1=url+'s'
print("正在获取歌曲信息.....")
hash=re.findall('#hash=(.*?)&',url_1)[0]
album_id=re.findall('&album_id=(.*?)s',url_1)[0]
song_url=f"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hash}&dfid=4XTDlO0Tjyl827K26B2JOWFJ&appid=1014&mid=36cafbb62a65fbbc7ab3480162172741&platid=4&album_id={album_id}&_=1649986632571"
response=requests.get(headers=headers,url=song_url).json()
mv_id=response['data']['video_id']
vedio_url=f'https://www.kugou.com/mvweb/html/mv_{mv_id}.html'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
vedio_response=requests.get(url=vedio_url,headers=headers,verify=False).text
mv_hash=re.findall('mv_hash = "(.*?)",',vedio_response)[0]
mv_title=re.findall('mv_name = "(.*?)",',vedio_response)[0]
title =mv_title.replace(' ','_')
mv_url=f'http://m.kugou.com/app/i/mv.php?cmd=100&hash={mv_hash}&ismp3=1&ext=mp4'
print("正在下载音乐....")
mv_response=requests.get(url=mv_url,headers=headers).json()
mv_add=mv_response['mvdata']['le']['downurl']
mv_content=requests.get(url=mv_add,headers=headers).content
with open('01.mp4',mode='wb')as f:
    f.write(mv_content)
a='01.mp4'
b='02.m4a'
c=title+'.mp3'
os.system('ffmpeg.exe -i '+a+' -vn -codec copy '+b)
os.system('ffmpeg.exe -i '+b+' -y -acodec libmp3lame -aq 0 '+c)
os.remove('01.mp4')
os.remove('02.m4a')
print("音乐下载完成....")


