import os
import time

"""If find the file named Download_list.txt now remove it"""

_path_ = os.path.abspath('.')
_FileJudge_ = os.listdir(_path_)
if os.path.exists(_path_+'Download_list.txt'):
    os.remove('Download_list.txt')
#if not os.path.exists(_path_+"\\下载"):
#    os.mkdir(_path_+"\\下载")

def get_file_from_cmd0(link, filename, headers):
    filename = fr"{filename}"
    exe_path = fr"{os.path.abspath('.')}\aria2c.exe"
    headers_keys = list(headers.keys())
    order = f'{exe_path} -o "{filename}" -s16 -x10 "{link}"'     #single download mode
    if len(headers_keys) != 0:
        for i in headers_keys:
            order += f' --header "{i}:{headers[i]}"'
    __start__ = time.time()
    os.system(order)
    __end__ = time.time()
    print(f'Used Time:{__end__-__start__}')
def get_file_from_cmd1():
    exe_path = os.path.abspath('.') + '\\aria2c.exe'
    order = f'{exe_path} -s16 -x10 --input-file=Download_list.txt'  # batch download mode
    __start__ = time.time()
    os.system(order)
    __end__ = time.time()
    print(f'Used Time:{__end__-__start__}')
    os.remove('Download_list.txt')

def _message_(tolist_url,tolist_name,headers):
    _WriteAdd_ = f"{tolist_url}\n out={tolist_name}\n"
    headers_keys = list(headers.keys())
    if len(headers_keys) != 0:
        for i in headers_keys:
            _WriteAdd_ += f" header={i}:{headers[i]}\n"
    f = open('Download_list.txt', 'a+')
    print(_WriteAdd_, file=f)
    f.close()










