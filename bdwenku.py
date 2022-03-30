import requests
import re
url = input('请输入url地址：')
print('url地址为：',url)
headers={
    "Referer":"https://wkstatic.bdimg.com/",
    "cookie":"buvid3=849B6928-BCED-C98D-6D6C-2EC34CA544E134077infoc; _uuid=E149C078-5067-1005-5BD0-97E4AA268B3E34851infoc; blackside_state=1; rpdid=|(k|RJYuuJRY0J'uYJkJ)|JJ~; buvid_fp_plain=994CE1A0-252A-26EA-64AB-85416E5FA87691069infoc; buvid_fp=62e09b1d54678d54a0cdffeec59051a7; buvid4=B7BE4592-BC12-9F0E-4D41-C4FB36B22B2217308-022012421-ccocVM+OlP2Qrps8ranvZA%3D%3D; i-wanna-go-back=-1; b_ut=7; LIVE_BUVID=AUTO9916435423786827; CURRENT_BLACKGAP=0; nostalgia_conf=-1; fingerprint=a623c0f07eeeb39d402e8548b2cc4a31; CURRENT_FNVAL=4048; PVID=3; b_lsid=414E82EF_17FAC87C141; innersign=1; sid=ijf3p2iw",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
}
print("正在获取文件地址.....")
response=requests.get(url=url,headers=headers)
html=response.text
urls=re.findall('https://wkimg.bdimg.com/img/.*?new=.*?&w=.*?&p=.*?',html)
for url_img in urls:
    file_name = re.findall('"title":"(.*?)"', html)[1]
    response_img = requests.get(url=url_img, headers=headers)
    with open(file_name+'.png','wb')as f:
        f.write(response_img.content)
print("文件已保存")
