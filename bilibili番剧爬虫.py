# coding=utf8
import os
import requests
import json
import re
import time
import pprint
import Aria2_Download_02

_path_ = os.path.abspath('.')
_FileJudge_ = os.listdir(_path_)
if not os.path.exists(f"{_path_}\\番剧"):
    os.mkdir(f"{_path_}\\番剧")

url = input("请输入番剧的网页地址:")

headers = {
    "Origin": "https://www.bilibili.com",
    "Referer": "https://www.bilibili.com/",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

print("正在请求网页源代码")
response_url_all = requests.get(url, headers)
print("成功")

print("正在分析源代码,寻找番剧基本信息")
response_url_1 = requests.utils.unquote(response_url_all.text)
response_url_1 = response_url_1.replace(r'\u002F', '/')
#print(response_url_1)
find_data_ = re.findall('window.__INITIAL_STATE__=(.*?),"viewAngle"', response_url_1)[0] + "}"
find_data = json.loads(find_data_)
#pprint.pprint(find_data)
lisy_all = find_data["epList"]
#pprint.pprint(lisy_all)
tanpy_list, guone_list, adid_list, juyse_list = [], [], [], []
for i in range(len(lisy_all)):
    tanpy_list.append(lisy_all[i]['share_copy'])
    guone_list.append(lisy_all[i]["id"])
    adid_list.append(lisy_all[i]["aid"])
    juyse_list.append(lisy_all[i]["cid"])
#print(tanpy_list)
#print(guone_list)

title = find_data["mediaInfo"]["season_title"]
title = title.replace('"', "'")
title = title.replace(':', ";")
title = title.replace('\\u002F', "-")
title = title.replace('\\', "-")
title = title.replace('|', "-")
title = title.replace('/', "-")
if title == '' or title == ' ':
    title = 'Untitled'
print(f"成功,番剧名:{title},集数:{len(tanpy_list)}")
mode = 0            #在这改下载模式
for i in range(len(tanpy_list)):
    print(f"正在爬取{tanpy_list[i]}")
    apiurl = f"https://api.bilibili.com//pgc/player/web/v2/playurl?support_multi_audio=true&avid={adid_list[i]}&cid={juyse_list[i]}&qn=80&fnver=0&fnval=4048&fourk=1&gaia_source=&from_client=BROWSER&ep_id={guone_list[i]}&session=4c33b91d224a9475d21ebeab700e2a19&drm_tech_type=2"
    response_vaall = requests.get(apiurl, headers).text
    response_vaall = json.loads(response_vaall)
    #pprint.pprint(response_vaall)
    video_url = response_vaall["result"]["video_info"]["dash"]["video"][0]["backupUrl"][0]
    audio_url = response_vaall["result"]["video_info"]["dash"]["audio"][0]["backupUrl"][0]
    print("已爬取到视频音频地址")
    if mode == 1:
        print("采用模式一下载")
        video = requests.get(video_url, headers).content
        with open("__1__.mp4", mode="wb") as f:
            f.write(video)
        audio = requests.get(audio_url, headers).content
        with open("__1__.mp3", mode="wb") as f:
            f.write(audio)
    else:
        print("不采用模式一下载")
        Aria2_Download_02._message_(video_url, "__1__.mp4", headers)
        Aria2_Download_02._message_(audio_url, "__1__.mp3", headers)
        Aria2_Download_02.get_file_from_cmd1()
    print("成功\n开始合成视频")
    if not os.path.exists(f"{_path_}\\番剧\\{title}"):
        os.mkdir(f"{_path_}\\番剧\\{title}")
    os.system(f'ffmpeg.exe -i "{_path_}\\__1__.mp4" -i "{_path_}\\__1__.mp3" -c copy "{_path_}\\番剧\\{title}\\{tanpy_list[i]}.mp4"')
    print("成功")
    os.remove("__1__.mp3")
    os.remove("__1__.mp4")
    time.sleep(3)
print("全部结束")

