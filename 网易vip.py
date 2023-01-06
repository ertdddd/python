import os
import re
import requests
url = input('请输入url地址：')
url_1=url.replace('/#','')
print("正在获取音频.....")
headers1={
    "Referer":"https://music.163.com/",
    "cookie":"buvid3=849B6928-BCED-C98D-6D6C-2EC34CA544E134077infoc; _uuid=E149C078-5067-1005-5BD0-97E4AA268B3E34851infoc; blackside_state=1; rpdid=|(k|RJYuuJRY0J'uYJkJ)|JJ~; buvid_fp_plain=994CE1A0-252A-26EA-64AB-85416E5FA87691069infoc; buvid_fp=62e09b1d54678d54a0cdffeec59051a7; buvid4=B7BE4592-BC12-9F0E-4D41-C4FB36B22B2217308-022012421-ccocVM+OlP2Qrps8ranvZA%3D%3D; i-wanna-go-back=-1; b_ut=7; LIVE_BUVID=AUTO9916435423786827; CURRENT_BLACKGAP=0; nostalgia_conf=-1; fingerprint=a623c0f07eeeb39d402e8548b2cc4a31; CURRENT_FNVAL=4048; PVID=3; b_lsid=414E82EF_17FAC87C141; innersign=1; sid=ijf3p2iw",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
}
headers2={
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-platform':'"Windows"',
    'referer':'https://music.163.com/',
    'cookie':'_ntes_nuid=5ee9ad10667edb829042238a195f8a73; NMTID=00OB6_z2x1LuDgD1Em2oe2tPROvG8kAAAF8EXci2g; WEVNSM=1.0.0; WNMCID=yqphut.1632380593294.01.0; WM_TID=3ZaE+YaRg8VERBAQUUNq9FMWej8JKQFK; _iuqxldmzr_=32; bitrate=320000; _ntes_nnid=5ee9ad10667edb829042238a195f8a73,1664632341579; NTES_P_UTID=DpkPlpP3QE8HW1dUu9KzJPUVen0D7BAs|1671799886; P_INFO=m13636900054_1@163.com|1671799886|0|partner|00&99|fuj&1671279045&partner#fuj&350500#10#0#0|136054&1||13636900054@163.com; JSESSIONID-WYYY=yZ3h3/Kq/SHG5vDRik4VTJnb\p0z8TpwQs\zDZ5X1vSdwozPjzymCujDpb1K368b1uW\5Pr3SPdmQ1TXXbppFMpZi/3o3C3E1HHXlx4pEmu+xPARbp1f\KfWgipijl9xIKT44j8Z8mFhyIkrf\D9sNlktPICBoFGokVfI2u\WI\l\ECQ:1672100818847; WM_NI=rw13henBNngm26rjZ1/rs4CQyOlh2GWyoP35k+CFRLgYdAi63DLPBVokNiMMOywZJFQM8CqZgf3kLi8zxD8Q1ko0A/nTz96D3Tg9coVcGUJw8BQqZTVhowVJc6J10gVuZlM=; WM_NIKE=9ca17ae2e6ffcda170e2e6eed3c143e9bb96d2d070acb48fa3c45a838f9e86d169afbd9bdab6688de989d5c72af0fea7c3b92ab2a9ffd4eb6fae9e828fe667f2eabe8bd93bedaebdd5c25bbb91a489b14d95a7a1b1b23fa9f58da7d148a587aca2ec3ef19c84b1c15eadb5828ad0478da7b9bbc94e9393f8a4f452a5bafd8ccf63fca6b8a5bb5bf3b5a1d1c425ae8cb6dab550f18ca9dae26596bd89b6c97dfc9e9f92d96096b8a198d542a1ea86d2b36d96ab968dd037e2a3; playerid=60580964',
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
response_1=requests.get(url=url_1,headers=headers1)
MV=re.findall('<a title="播放mv" href="(.*?)"',response_1.text)[0]
url_2="https://music.163.com"+MV
response=requests.get(url=url_2,headers=headers2)
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