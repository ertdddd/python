import re
import requests
url = input('请输入url地址：')
url_1=url.replace('/#','')
print("正在获取音频.....")
headers={
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-platform':'"Windows"',
    'referer':'https://music.163.com/',
    'cookie':'_ntes_nuid=5ee9ad10667edb829042238a195f8a73; NMTID=00OB6_z2x1LuDgD1Em2oe2tPROvG8kAAAF8EXci2g; WEVNSM=1.0.0; WNMCID=yqphut.1632380593294.01.0; WM_TID=3ZaE+YaRg8VERBAQUUNq9FMWej8JKQFK; _iuqxldmzr_=32; bitrate=320000; _ntes_nnid=5ee9ad10667edb829042238a195f8a73,1664632341579; NTES_P_UTID=DpkPlpP3QE8HW1dUu9KzJPUVen0D7BAs|1671799886; P_INFO=m13636900054_1@163.com|1671799886|0|partner|00&99|fuj&1671279045&partner#fuj&350500#10#0#0|136054&1||13636900054@163.com; JSESSIONID-WYYY=yZ3h3/Kq/SHG5vDRik4VTJnb\p0z8TpwQs\zDZ5X1vSdwozPjzymCujDpb1K368b1uW\5Pr3SPdmQ1TXXbppFMpZi/3o3C3E1HHXlx4pEmu+xPARbp1f\KfWgipijl9xIKT44j8Z8mFhyIkrf\D9sNlktPICBoFGokVfI2u\WI\l\ECQ:1672100818847; WM_NI=rw13henBNngm26rjZ1/rs4CQyOlh2GWyoP35k+CFRLgYdAi63DLPBVokNiMMOywZJFQM8CqZgf3kLi8zxD8Q1ko0A/nTz96D3Tg9coVcGUJw8BQqZTVhowVJc6J10gVuZlM=; WM_NIKE=9ca17ae2e6ffcda170e2e6eed3c143e9bb96d2d070acb48fa3c45a838f9e86d169afbd9bdab6688de989d5c72af0fea7c3b92ab2a9ffd4eb6fae9e828fe667f2eabe8bd93bedaebdd5c25bbb91a489b14d95a7a1b1b23fa9f58da7d148a587aca2ec3ef19c84b1c15eadb5828ad0478da7b9bbc94e9393f8a4f452a5bafd8ccf63fca6b8a5bb5bf3b5a1d1c425ae8cb6dab550f18ca9dae26596bd89b6c97dfc9e9f92d96096b8a198d542a1ea86d2b36d96ab968dd037e2a3; playerid=60580964',
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
response=requests.get(url=url_1,headers=headers)
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
