import requests
import re
import json
import os
url = input('请输入url地址：')
print('url地址为：',url)
headers={
    "Referer":"https://www.bilibili.com/",
    "cookie":"buvid3=849B6928-BCED-C98D-6D6C-2EC34CA544E134077infoc; _uuid=E149C078-5067-1005-5BD0-97E4AA268B3E34851infoc; blackside_state=1; rpdid=|(k|RJYuuJRY0J'uYJkJ)|JJ~; buvid_fp_plain=994CE1A0-252A-26EA-64AB-85416E5FA87691069infoc; buvid_fp=62e09b1d54678d54a0cdffeec59051a7; buvid4=B7BE4592-BC12-9F0E-4D41-C4FB36B22B2217308-022012421-ccocVM+OlP2Qrps8ranvZA%3D%3D; i-wanna-go-back=-1; b_ut=7; LIVE_BUVID=AUTO9916435423786827; CURRENT_BLACKGAP=0; nostalgia_conf=-1; fingerprint=a623c0f07eeeb39d402e8548b2cc4a31; CURRENT_FNVAL=4048; PVID=3; b_lsid=414E82EF_17FAC87C141; innersign=1; sid=ijf3p2iw",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
}
print("正在获取视频地址.....")
response=requests.get(url=url,headers=headers)
title=re.findall('<h1 title="(.*?)" class="video-title">',response.text)[0]
title = title.replace(' ','_')
playinfo=re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
jsondata=json.loads(playinfo)
audiourl=jsondata['data']['dash']['audio'][0]['backupUrl'][0]
videourl=jsondata['data']['dash']['video'][0]['backupUrl'][0]
print("已获取到视频地址，正在开始下载，请稍后.....")
audio_content=requests.get(url=audiourl,headers=headers).content
video_content=requests.get(url=videourl,headers=headers).content
#mode是保存方式
print("正在合成视频....")
with open('_1_.mp4',mode='wb')as f:
    f.write(video_content)
with open('_2_.mp3',mode='wb')as f:
    f.write(audio_content)
a = '_1_.mp4'
b = '_2_.mp3'
c = title+'.mp4'
os.system('ffmpeg.exe -i '+a+' -i '+b+' -c copy '+c)

print(title,"\n合成已完成")
os.remove('_1_.mp4')
os.remove('_2_.mp3')
