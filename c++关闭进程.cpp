#include <Windows.h>
#include <TlHelp32.h>
#include<iostream>
#pragma comment( linker, "/subsystem:windows /entry:mainCRTStartup" )
using namespace std;
/******************************
 *  @brief     ��������
 *  @param     szImageName:������
 *  @note      ͷ�ļ��� #include <Windows.h> #include <TlHelp32.h>
 *  @Sample usage:	KillProcess(������);
 * @author     xbebhxx3
 * @version    2.0
 * @date       2022/3/15
# Copyright (c) 2022-2077 xbebhxx3
******************************/
void KillProcess(char* szImageName){
	PROCESSENTRY32 pe = {sizeof(PROCESSENTRY32) }; //��ý����б�
	HANDLE hProcess = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);//�������
	BOOL bRet = Process32First(hProcess,&pe);//���������е�һ��������Ϣ
	while(bRet){//�жϲ������һ�����̣���������
		if(lstrcmp(szImageName,pe.szExeFile)==0) {//�ж��ǲ���Ҫ�����Ľ���
			TerminateProcess(OpenProcess(PROCESS_ALL_ACCESS, FALSE,pe.th32ProcessID), 0);//�򿪽��̲�ɱ��
		}
		bRet = Process32Next(hProcess,&pe);//��һ������
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
	KillProcess("EasiNote.exe");//����
	system("start D:\\EasiNote5\\swenlauncher\\swenlauncher.exe");
	system("pause");
} 
