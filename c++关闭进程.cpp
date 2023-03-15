#include <Windows.h>
#include <TlHelp32.h>
#include<iostream>
#pragma comment( linker, "/subsystem:windows /entry:mainCRTStartup" )
using namespace std;
/******************************
 *  @brief     结束进程
 *  @param     szImageName:进程名
 *  @note      头文件： #include <Windows.h> #include <TlHelp32.h>
 *  @Sample usage:	KillProcess(进程名);
 * @author     xbebhxx3
 * @version    2.0
 * @date       2022/3/15
# Copyright (c) 2022-2077 xbebhxx3
******************************/
void KillProcess(char* szImageName){
	PROCESSENTRY32 pe = {sizeof(PROCESSENTRY32) }; //获得进程列表
	HANDLE hProcess = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);//拍摄快照
	BOOL bRet = Process32First(hProcess,&pe);//检索快照中第一个进程信息
	while(bRet){//判断不是最后一个进程，历遍所有
		if(lstrcmp(szImageName,pe.szExeFile)==0) {//判断是不是要结束的进程
			TerminateProcess(OpenProcess(PROCESS_ALL_ACCESS, FALSE,pe.th32ProcessID), 0);//打开进程并杀死
		}
		bRet = Process32Next(hProcess,&pe);//下一个进程
	}
	return;
}
int main(){
	HWND hwnd;
	hwnd=FindWindow("ConsoleWindowClass",NULL);
	if(hwnd)
	{
		ShowWindow(hwnd,SW_HIDE);
	}
	_sleep(60*1000);
	KillProcess("EasiNote.exe");//调用
	system("start D:\\EasiNote5\\swenlauncher\\swenlauncher.exe");
	system("pause");
} 
