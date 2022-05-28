import os
import re
import requests
url = input('请输入url地址：')
url_1=url.replace('/#','')
print("正在获取音频.....")
headers={
    "Referer":"https://music.163.com/",
    "cookie":"buvid3=849B6928-BCED-C98D-6D6C-2EC34CA544E134077infoc; _uuid=E149C078-5067-1005-5BD0-97E4AA268B3E34851infoc; blackside_state=1; rpdid=|(k|RJYuuJRY0J'uYJkJ)|JJ~; buvid_fp_plain=994CE1A0-252A-26EA-64AB-85416E5FA87691069infoc; buvid_fp=62e09b1d54678d54a0cdffeec59051a7; buvid4=B7BE4592-BC12-9F0E-4D41-C4FB36B22B2217308-022012421-ccocVM+OlP2Qrps8ranvZA%3D%3D; i-wanna-go-back=-1; b_ut=7; LIVE_BUVID=AUTO9916435423786827; CURRENT_BLACKGAP=0; nostalgia_conf=-1; fingerprint=a623c0f07eeeb39d402e8548b2cc4a31; CURRENT_FNVAL=4048; PVID=3; b_lsid=414E82EF_17FAC87C141; innersign=1; sid=ijf3p2iw",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
}
response_1=requests.get(url_1)
MV=re.findall('<a title="播放mv" href="(.*?)"',response_1.text)[0]
url_2="https://music.163.com"+MV
response=requests.get(url_2)
title=re.findall('<meta property="og:title" content="(.*?)" />',response.text)[0]
title = title.replace(' ','_')
html=re.findall('<meta property="og:video" content="(.*?)" />',response.text)[0]
html_1=re.sub('%3A',':',html)
html_2=re.sub('%2F','/',html_1)
html_3=re.sub('%3D','=',html_2)
html_4=re.sub('%2F','/',html_3)
html_5=re.sub('%3F','?',html_4)
html_6=re.sub('%26','&',html_5)
print("正在下载....")
response_2=requests.get(html_6)
music_data=response_2.content

with open('01'+ '.mp4', mode='wb') as f:
    f.write(music_data)
a='01.mp4'
b='02.m4a'
c=title+'.mp3'
os.system('ffmpeg.exe -i '+a+' -vn -codec copy '+b)
os.system('ffmpeg.exe -i '+b+' -y -acodec libmp3lame -aq 0 '+c)
os.remove('01.mp4')
os.remove('02.m4a')
print("音乐下载完成....")