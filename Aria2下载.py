import os
import time
from pyaria2 import Aria2RPC

"""look that!!!! mode0:single download mode , mode1:batch download mode"""
print("Welcome!\nThanks for your support!\nIf the download isn't successful,try to give the Referer!\n")
mode = input("mode0:single download mode , mode1:batch download mode[0/1]:")
tolist_url = input('Please give the File Download URL:')
tolist_name = input('Please give the File Name:')
tolist_referer = input("Please give the Referer(not have to):")

if mode == 1:
    write_content = ''
    while not tolist_name == '' and not tolist_url == '':
        if tolist_referer == '':
            write_content += tolist_url + '\n out=' + tolist_name + '\n'
        else:
            write_content += tolist_url + '\n out=' + tolist_name + '\n referer=' + tolist_referer + '\n'
        tolist_url = input("Please give next File Download URL:")
        tolist_name = input("Please give next File Name:")
        tolist_referer = input("Please give next Referer(not have to):")
    print(write_content)
    f = open('Download_list.txt','w')
    print(write_content,file=f)
    f.close()

def get_file_from_url(link,file_name):
    jsonrpc = Aria2RPC()
    set_dir = os.path.dirname(__file__)
    options = {'dir': set_dir, "out": file_name, }
    res = jsonrpc.addUri([link],options = options)

def get_file_from_cmd0(link,filename,referer):
    exe_path = os.path.abspath('.') + '\\aria2c.exe'
    if referer == '':
        order = exe_path + ' -o "' + filename + '" -s16 -x10 "' + link + '"'     #single download mode
    else:
        order = exe_path + ' -o "' + filename + '" -s16 -x10 "' + link + '" --referer=' + referer
    os.system(order)
def get_file_from_cmd1():
    exe_path = os.path.abspath('.') + '\\aria2c.exe'
    order = exe_path + ' --input-file=Download_list.txt'  # batch download mode
    os.system(order)

if mode == 1:
    if __name__ == '__main__':
        start = time.time()
        get_file_from_cmd1()
        end = time.time()
        print(f"Used time:{end - start:.2f}")
        os.remove('Download_list.txt')
elif mode == 0:
    if __name__ == '__main__':
        link = tolist_url
        filename = tolist_name

        start = time.time()
        get_file_from_cmd0(link,filename,referer=tolist_referer)
        end = time.time()
        print(f"Used time:{end-start:.2f}")










