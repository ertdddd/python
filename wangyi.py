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
response=requests.get(url_1)
#print(response.text)
html=response.text
audio_data=re.findall('<meta property="og:audio" content="https://music.163.com/song\?id=(.*?)"/',html)
title=re.findall('meta property="og:title" content="(.*?)" /',html)[0]
for music_id in audio_data:
    music_url='http://music.163.com/song/media/outer/url?id='+music_id
    response_2=requests.get(music_url)
    music_data=response_2.content
    with open(title+'.mp3',mode='wb')as f:
        f.write(music_data)
    print("音频获取已完成.....")
